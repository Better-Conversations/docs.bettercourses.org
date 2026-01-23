import pathlib
import subprocess
from datetime import datetime
import dateutil
from docutils import nodes
import os

gh_repo_url = "https://github.com/Better-Conversations/docs.bettercourses.org"
docs_site_url = "https://docs.bettercourses.org"

# Mapping of git author names/usernames to consistent display names
AUTHOR_NAME_MAP = {
    "chandima-d": "Chandima Dutton",
    "chandimad": "Chandima Dutton",
    "alexjcoles": "Alex Coles",
    "shivamphora": "Shivani Patel",
}


def normalize_author_name(name: str) -> str:
    """Normalize git author names to consistent display names."""
    return AUTHOR_NAME_MAP.get(name, name)


def create_header(document_reference, author_datetime, commit_datetime, git_sha, last_author):
    """Create the QMS header as a collapsible details element."""
    # Create a collapsible details element with accessibility attributes
    details_open = nodes.raw('', '<details class="qms-header" role="group" aria-label="Document information"><summary aria-expanded="false">Document Information</summary>', format='html')
    details_close = nodes.raw('', '</details>', format='html')

    header_list = nodes.bullet_list()

    # Document reference (file path)
    header_list += create_item("Reference", document_reference)

    # Last Edited By
    header_list += create_item("Last Edited By", last_author)

    # Last Edited (author date - when changes were made)
    header_list += create_item("Last Edited", author_datetime)

    # Effective from (commit date - when this version was approved/merged)
    header_list += create_item("Effective from", commit_datetime)

    # Git Commit with link to commit on GitHub
    commit_link = nodes.reference(refuri=f"{gh_repo_url}/commit/{git_sha}")
    commit_link += nodes.Text(git_sha)
    header_list += create_item("Git Commit", commit_link)

    # Document status note - deployed = approved
    note_para = nodes.paragraph()
    note_para += nodes.Text("This is the current approved version. Printed or downloaded copies may be superseded; refer to ")
    docs_link = nodes.reference(refuri=docs_site_url)
    docs_link += nodes.Text("docs.bettercourses.org")
    note_para += docs_link
    note_para += nodes.Text(" for the authoritative version.")
    header_list += create_item("Note", note_para)

    # Return wrapped in details element
    container = nodes.container()
    container += details_open
    container += header_list
    container += details_close

    return container


def create_item(label, value: str | nodes.Node):
    if isinstance(value, str):
        value = nodes.Text(value)

    item = nodes.list_item()
    para = nodes.paragraph()
    strong = nodes.strong(text=f"{label}: ")
    para += strong

    # If value is a paragraph, extract its children to avoid nested paragraphs
    if isinstance(value, nodes.paragraph):
        for child in value.children:
            para += child
    else:
        para += value

    item += para
    return item


def format_datetime(date: datetime) -> str:
    """Format datetime as '23rd January 2026 at 13:14'."""
    day = date.day
    if 11 <= day <= 13:
        suffix = 'th'
    else:
        suffix = ['th', 'st', 'nd', 'rd', 'th'][min(day % 10, 4)]

    return f"{day}{suffix} {date.strftime('%B %Y')} at {date.strftime('%H:%M')}"


def get_git_info_for_file(path):
    """Get git information for a specific file."""
    # Convert absolute path to relative path within the repository
    try:
        repo_path = subprocess.check_output(
            ["git", "rev-parse", "--show-toplevel"],
            text=True
        ).strip()
        relative_path = os.path.relpath(path, repo_path) if os.path.isabs(path) else path
    except (subprocess.SubprocessError, FileNotFoundError):
        relative_path = os.path.basename(path)

    # Note that git information will be for the last commit that touched
    # this file, if the file is changed but not committed, this will not
    # be reflected in the header.
    try:
        # Single git call with combined format: sha|author_date|commit_date|author_name
        # Author date (%aI) = when the author made the changes
        # Commit date (%cI) = when the commit was applied (e.g., merged/rebased)
        git_output = subprocess.check_output([
            "git", "log", "-n", "1", "--format=%h|%aI|%cI|%aN", "--", relative_path
        ], text=True, stderr=subprocess.STDOUT).strip()

        # Handle case where file has no git history (empty output)
        if not git_output:
            return "unknown", None, None, "unknown"

        parts = git_output.split("|")
        if len(parts) != 4:
            return "unknown", None, None, "unknown"

        git_sha, author_date, commit_date, author_name = parts
        # Normalize the author name for consistent display
        author_name = normalize_author_name(author_name)

        return git_sha, author_date, commit_date, author_name
    except subprocess.CalledProcessError:
        return "unknown", None, None, "unknown"


def add_qms_header_to_doctree(app, doctree, docname):
    """Add QMS header to every page automatically during doctree-resolved."""
    # Only inject the header for HTML builds to avoid issues with PDF and other formats
    if app.builder.format != 'html':
        return
    
    # Get the source file path
    source_path = app.env.doc2path(docname)

    git_sha, author_date, commit_date, author_name = get_git_info_for_file(source_path)

    # Document reference is the docname path with source file extension
    # e.g., "about/index.rst" or "documentation/guide.md"
    source_file = pathlib.Path(source_path)
    document_reference = f"{docname}{source_file.suffix}"

    # Format author date (when changes were made)
    if author_date:
        parsed_author_date = dateutil.parser.isoparse(author_date)
        author_datetime = format_datetime(parsed_author_date)
    else:
        author_datetime = "unknown"

    # Format commit date (when changes were approved/merged)
    if commit_date:
        parsed_commit_date = dateutil.parser.isoparse(commit_date)
        commit_datetime = format_datetime(parsed_commit_date)
    else:
        commit_datetime = "unknown"

    header = create_header(
        document_reference,
        author_datetime,
        commit_datetime,
        git_sha,
        author_name
    )

    # Append the header to the end of the document
    doctree.append(header)


def setup(app):
    # Auto-inject QMS header at the bottom of every page
    app.connect('doctree-resolved', add_qms_header_to_doctree)

    return {
        'version': '0.5',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
