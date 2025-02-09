import os
import glob
from docutils.parsers.rst import Directive
from docutils import nodes


def get_document_list(source_dir):
    """
    Dynamically find all .rst and .md files in the source directory.
    """
    rst_files = glob.glob(os.path.join(source_dir, "**/*.rst"), recursive=True)
    md_files = glob.glob(os.path.join(source_dir, "**/*.md"), recursive=True)

    # Normalize paths and strip extensions to match Sphinx docnames
    all_files = rst_files + md_files
    docnames = [
        os.path.relpath(f, source_dir).replace("\\", "/")
        for f in all_files
    ]
    return docnames

def generate_llms_full(docnames: list[str]):
    """
    Generate the llms_full.txt file containing the raw content of all .rst and .md files.
    
    Args:
        docnames: List of document paths relative to the source directory
    """
    source_dir = os.path.abspath("./source")
    output = []
    
    for doc in docnames:
        full_path = os.path.join(source_dir, doc)
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
                output.append(f"\n\n### File: {doc}\n\n{content}")
        except FileNotFoundError:
            print(f"Warning: Could not find file {full_path}")
        except Exception as e:
            print(f"Error reading {full_path}: {str(e)}")
            
    # Write all content to the output file
    with open("llms_full.txt", "w", encoding='utf-8') as f:
        f.write("\n".join(output))
        
    print(f"llms_full.txt file has been created with content from {len(docnames)} documents.")

def get_summary(doc_path: str) -> str:
    """Extract summary from a document if it exists."""
    try:
        with open(doc_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Look for summary directive in rst files
        if doc_path.endswith('.rst'):
            if '.. summary::' in content:
                summary_start = content.index('.. summary::') + 11
                # Skip any whitespace or newlines after the directive
                while summary_start < len(content) and content[summary_start].isspace():
                    summary_start += 1
                summary_end = content.find('\n\n', summary_start)
                if summary_end == -1:
                    summary_end = len(content)
                # Clean up the summary text
                summary = content[summary_start:summary_end].replace('\n', ' ').strip()
                return summary
                
        # Look for summary in markdown files
        elif doc_path.endswith('.md'):
            if '<!--summary:' in content and '-->' in content:
                summary_start = content.index('<!--summary:') + 11
                summary_end = content.index('-->', summary_start)
                return content[summary_start:summary_end].strip()
                
    except Exception as e:
        print(f"Error reading summary from {doc_path}: {str(e)}")
    
    return ""

def generate_llms(docnames: list[str]):
    """
    Generate the llms.txt file with the file names (with links and without file type) and a summary if available.
    
    Args:
        docnames: List of document paths relative to the source directory
    """

    source_dir = os.path.abspath("./source")
    output = []
    
    # Add title and description
    output.append("# Better Conversations Foundation")
    output.append("\n> Helping people connect on a human level")
    output.append("\nThe Better Conversations Foundation helps people around the world have better conversations in their professional and private lives through training, resources and community.")

    # Group documents by directory
    sections = {}
    for doc in docnames:
        directory = os.path.dirname(doc)
        if not directory:
            directory = "root"
        if directory not in sections:
            sections[directory] = []
        sections[directory].append(doc)

    # Generate sections and links with summaries
    for section, docs in sorted(sections.items()):
        if section == "root":
            section_title = "Main"
        else:
            section_title = section.replace("/", " - ").title()
            
        output.append(f"\n## {section_title}")
        
        for doc in sorted(docs):
            # Create link title by using filename without extension
            filename = os.path.basename(doc)
            link_title = os.path.splitext(filename)[0].replace("-", " ").replace("_", " ").title()
            
            # Create relative URL path
            url = "/" + doc.rsplit(".", 1)[0] + ".html"
            
            # Get summary if available
            summary = get_summary(os.path.join(source_dir, doc))
            
            # Create output line with optional summary
            if summary:
                output.append(f"- [{link_title}]({url}): {summary}")
            else:
                output.append(f"- [{link_title}]({url})")

    # Write output to llms.txt
    with open("llms.txt", "w", encoding='utf-8') as f:
        f.write("\n".join(output))
        
    print("llms.txt file has been created with formatted content and summaries.")

class Summary(Directive):
    """
    Directive for adding a summary that will be included in llms.txt but not rendered in HTML.
    
    Usage:
    .. summary::
        This is a summary of the page that will appear in llms.txt
    """
    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = True

    def run(self):
        # Create an empty node - this ensures the summary doesn't appear in HTML
        return [nodes.comment('', '\n'.join(self.content))]

def setup(app):
    app.add_directive('summary', Summary)
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }




if __name__ == "__main__":
    # Define the source directory to scan
    source_dir = os.path.abspath("./source")  # Change this to your desired source directory

    # Check if the directory exists
    if not os.path.exists(source_dir):
        print(f"Source directory '{source_dir}' does not exist. Please create it and add some .rst or .md files.")
        exit(1)

    # Call the function and get document names
    documents = get_document_list(source_dir)

    # Define the output file to write the document names
    output_file = os.path.abspath("document_list.txt")

    # Write results to the output file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("Found documents:\n")
        for doc in documents:
            f.write(f"{doc}\n")

    # Print success message
    print(f"Document names have been written to '{output_file}'.")

    generate_llms_full(documents)
    generate_llms(documents)