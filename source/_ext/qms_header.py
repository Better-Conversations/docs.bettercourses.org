import pathlib
import subprocess
import sys
from datetime import datetime
import dateutil
from docutils.parsers.rst import Directive
from docutils import nodes
import os

gh_repo_url = "https://github.com/Better-Conversations/betterconversations.foundation"

# Mapping of git author names/usernames to consistent display names
AUTHOR_NAME_MAP = {
    "chandima-d": "Chandima Dutton",
    "chandimad": "Chandima Dutton",
    "alexjcoles": "Alex Coles",
    "shivamphora": "Shivam Phora",
}


def normalize_author_name(name: str) -> str:
    """Normalize git author names to consistent display names."""
    return AUTHOR_NAME_MAP.get(name, name)


def create_header(document_reference, git_commit_datetime, git_sha, last_author):
    """Create the QMS header as a collapsible details element."""
    # Create a collapsible details element
    details_open = nodes.raw('', '<details class="qms-header"><summary>Document Information</summary>', format='html')
    details_close = nodes.raw('', '</details>', format='html')

    header_list = nodes.bullet_list()

    # Document reference
    header_list += create_item("Reference", document_reference)

    # Last Edited By (moved to second position)
    header_list += create_item("Last Edited By", last_author)

    # Last Edited Date with full date/time stamp
    header_list += create_item("Last Edited Date", git_commit_datetime)

    # Git Commit with link to commit on GitHub
    commit_link = nodes.reference(refuri=f"{gh_repo_url}/commit/{git_sha}")
    commit_link += nodes.Text(git_sha)
    header_list += create_item("Git Commit", commit_link)

    # Only valid online - create a paragraph with mixed text and link
    note_para = nodes.paragraph()
    note_para += nodes.Text("Please refer to ")
    docs_link = nodes.reference(refuri="https://docs.bettercourses.org")
    docs_link += nodes.Text("docs.bettercourses.org")
    note_para += docs_link
    note_para += nodes.Text(" for valid technical documentation. Printed or downloaded copies may not reflect the current BCF documentation.")
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
        last_relevant_git_sha = subprocess.check_output([
            "git", "log", "-n", "1", "--format=%h", "--", relative_path
        ], text=True, stderr=subprocess.STDOUT).strip()

        # Use author date (%aI) - when changes were originally written
        # (not committer date which can differ with rebases/cherry-picks)
        last_updated_date = subprocess.check_output([
            "git", "log", "-n", "1", "--format=%aI", "--", relative_path
        ], text=True, stderr=subprocess.STDOUT).strip()

        # Use author name (%aN) to match the author date
        last_author = subprocess.check_output([
            "git", "log", "-n", "1", "--format=%aN", "--", relative_path
        ], text=True, stderr=subprocess.STDOUT).strip()

        # Handle case where file has no git history (empty output)
        if not last_relevant_git_sha or not last_updated_date:
            last_relevant_git_sha = "unknown"
            last_updated_date = None
            last_author = "unknown"
        else:
            # Normalize the author name for consistent display
            last_author = normalize_author_name(last_author)
    except subprocess.CalledProcessError:
        last_relevant_git_sha = "unknown"
        last_updated_date = None
        last_author = "unknown"

    return last_relevant_git_sha, last_updated_date, last_author


class QMSHeader(Directive):
    """Directive for manually inserting QMS header (kept for backwards compatibility)."""
    def run(self):
        path = self.state.document.current_source
        git_sha, last_updated_date, last_author = get_git_info_for_file(path)
        document_reference = pathlib.Path(path).stem

        if last_updated_date:
            parsed_date = dateutil.parser.isoparse(last_updated_date)
            git_commit_datetime = format_datetime(parsed_date)
        else:
            git_commit_datetime = "unknown"

        return [create_header(
            document_reference,
            git_commit_datetime,
            git_sha,
            last_author
        )]


def add_qms_header_to_doctree(app, doctree, docname):
    """Add QMS header to every page automatically during doctree-resolved."""
    # Get the source file path
    source_path = app.env.doc2path(docname)

    git_sha, last_updated_date, last_author = get_git_info_for_file(source_path)
    document_reference = pathlib.Path(source_path).stem

    if last_updated_date:
        parsed_date = dateutil.parser.isoparse(last_updated_date)
        git_commit_datetime = format_datetime(parsed_date)
    else:
        git_commit_datetime = "unknown"

    header = create_header(
        document_reference,
        git_commit_datetime,
        git_sha,
        last_author
    )

    # Append the header to the end of the document
    doctree.append(header)


def setup(app):
    # Keep the directive for backwards compatibility
    app.add_directive('qms_header', QMSHeader)

    # Auto-inject QMS header at the bottom of every page
    app.connect('doctree-resolved', add_qms_header_to_doctree)

    return {
        'version': '0.2',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
