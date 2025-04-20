import pathlib
import subprocess
import sys
from datetime import datetime
import dateutil
from docutils.parsers.rst import Directive
from docutils import nodes
import os

gh_repo_url = "https://github.com/Better-Conversations/betterconversations.foundation"


def create_header(document_reference, date, git_sha, last_author):
    header_list = nodes.bullet_list()

    # Document reference
    header_list += create_item("Reference", document_reference)
    header_list += create_item("Last Changed Date", date)

    # Revision (in form of git sha) with link to commit on GitHub
    rev_link = nodes.reference(refuri=f"{gh_repo_url}/commit/{git_sha}")
    rev_link += nodes.Text(git_sha)
    header_list += create_item("Git Version", rev_link)

    # Approved by
    header_list += create_item("Last Edited By", last_author)

    # Only valid online
    header_list += create_item("Note", "Document is only valid online at https://betterconversations.foundation.")

    return header_list


def create_item(label, value: str | nodes.Node):
    if isinstance(value, str):
        value = nodes.Text(value)

    item = nodes.list_item()
    para = nodes.paragraph()
    strong = nodes.strong(text=f"{label}: ")
    text = value
    para += strong
    para += text
    item += para
    return item


def format_date(date: datetime) -> str:
    # Get the day with the appropriate suffix (e.g., 1st, 2nd, 3rd, 4th)
    day = date.day
    if 11 <= day <= 13:
        suffix = 'th'
    else:
        suffix = ['th', 'st', 'nd', 'rd', 'th'][min(day % 10, 4)]

    # Format the date as desired
    formatted_date = f"{day}{suffix} {date.strftime('%B %Y')}"

    return formatted_date


class QMSHeader(Directive):
    def run(self):
        path = self.state.document.current_source

        # Convert absolute path to relative path within the repository
        # This is needed for GitHub Actions where paths include the full workspace path
        try:
            # First try to make the path relative to the current working directory
            repo_path = subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip()
            relative_path = os.path.relpath(path, repo_path) if os.path.isabs(path) else path
        except (subprocess.SubprocessError, FileNotFoundError):
            # If that fails, just use the filename which might work in simple cases
            relative_path = os.path.basename(path)

        # Note that git information will be for the last commit that touched
        # this file, if the file is changed but not committed, this will not
        # be reflected in the header.

        try:
            # Get latest commit sha for this file
            last_relevant_git_sha = subprocess.check_output([
                "git",
                "log",
                "-n", "1",
                "--format=%h",
                "--",
                relative_path
            ], text=True).strip()

            # Get last updated date for this file
            last_updated_date = subprocess.check_output([
                "git",
                "log",
                "-n", "1",
                "--format=%cI",
                "--",
                relative_path
            ], text=True).strip()

            # Get last author for this file, named by their git settings
            last_author = subprocess.check_output([
                "git",
                "log",
                "-n", "1",
                "--format=%cN",
                "--",
                relative_path
            ], text=True).strip()
        except subprocess.CalledProcessError:
            # Fallback if git commands fail
            last_relevant_git_sha = "unknown"
            last_updated_date = datetime.now().isoformat()
            last_author = "unknown"

        # Remove the file extension from the file name to get the document reference
        document_reference = pathlib.Path(self.state.document.current_source).stem

        if last_updated_date != "unknown":
            formatted_date = format_date(dateutil.parser.isoparse(last_updated_date))
        else:
            formatted_date = "unknown"

        return [create_header(
            document_reference,
            formatted_date,
            last_relevant_git_sha,
            last_author
        )]


def setup(app):
    app.add_directive('qms_header', QMSHeader)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
