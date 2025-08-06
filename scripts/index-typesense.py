#!/usr/bin/env python3
"""
Typesense indexer for Better Conversations Foundation Sphinx documentation
This is a Python fallback for environments where Docker is not available
"""

import os
import sys
import json
import time
import hashlib
from pathlib import Path
from urllib.parse import urljoin, urlparse
from typing import List, Dict, Any
from datetime import datetime

# Add parent directory to path to import from source/_ext
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    import typesense
    from bs4 import BeautifulSoup
    from dotenv import load_dotenv
except ImportError as e:
    print(f"Missing required package: {e}")
    print("Please install: pip install typesense beautifulsoup4 python-dotenv")
    sys.exit(1)

# Load environment variables
load_dotenv('.env.typesense')

class SphinxTypesenseIndexer:
    def __init__(self):
        """Initialize the Typesense client and configuration"""
        self.base_url = "https://betterconversations.foundation"
        self.build_dir = Path("build/html")
        
        # Initialize Typesense client
        self.client = typesense.Client({
            'api_key': os.getenv('TYPESENSE_API_KEY'),
            'nodes': [{
                'host': os.getenv('TYPESENSE_HOST', 'typesense.bettercourses.org'),
                'port': os.getenv('TYPESENSE_PORT', '443'),
                'protocol': os.getenv('TYPESENSE_PROTOCOL', 'https')
            }],
            'connection_timeout_seconds': 2
        })
        
        self.collection_name = 'bcf-content'
        
    def extract_text_from_html(self, html_content: str) -> Dict[str, Any]:
        """Extract structured content from HTML"""
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Find the main article content
        article = soup.find('article', class_='bd-article')
        if not article:
            article = soup.find('div', class_='bd-content')
        if not article:
            return None
            
        # Extract title
        title_elem = article.find('h1')
        title = title_elem.get_text(strip=True) if title_elem else "Untitled"
        
        # Remove the permalink anchors
        for permalink in article.find_all('a', class_='headerlink'):
            permalink.decompose()
            
        # Extract headings for hierarchy
        h1 = title
        h2_elems = article.find_all('h2')
        h2_texts = [h.get_text(strip=True) for h in h2_elems[:3]]  # First 3 h2s
        
        # Extract main content text
        # Remove script and style elements
        for script in article(['script', 'style']):
            script.decompose()
            
        # Get text content
        content_text = article.get_text(separator=' ', strip=True)
        
        # Create excerpt (first 200 chars)
        excerpt = content_text[:200] + "..." if len(content_text) > 200 else content_text
        
        # Extract any tags if present
        tags = []
        tag_links = soup.find_all('a', href=lambda x: x and '/_tags/' in x)
        for tag_link in tag_links:
            tag_text = tag_link.get_text(strip=True)
            if tag_text and tag_text not in tags:
                tags.append(tag_text)
        
        return {
            'title': title,
            'content': content_text,
            'excerpt': excerpt,
            'hierarchy': {
                'lvl0': h1,
                'lvl1': h2_texts[0] if h2_texts else None,
                'lvl2': h2_texts[1] if len(h2_texts) > 1 else None
            },
            'tags': tags
        }
    
    def get_html_files(self) -> List[Path]:
        """Get all HTML files to index"""
        if not self.build_dir.exists():
            print(f"Build directory {self.build_dir} does not exist")
            return []
            
        # Files to exclude
        exclude_patterns = [
            'genindex.html',
            'search.html',
            'searchindex.js',
            '404.html',
            '_static',
            '_sources',
            '.doctrees'
        ]
        
        html_files = []
        for html_file in self.build_dir.rglob('*.html'):
            # Skip excluded files
            if any(pattern in str(html_file) for pattern in exclude_patterns):
                continue
            if html_file.name.startswith('_'):
                continue
                
            html_files.append(html_file)
            
        return html_files
    
    def create_document(self, file_path: Path, content_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a Typesense document from extracted content"""
        # Generate document ID with 'docs-' prefix
        relative_path = file_path.relative_to(self.build_dir)
        doc_id = 'docs-' + str(relative_path).replace('.html', '').replace('/', '-')
        
        # Create URL slug
        slug = '/' + str(relative_path).replace('\\', '/')
        full_url = urljoin(self.base_url, slug)
        
        # Get file modification time as timestamp
        timestamp = int(file_path.stat().st_mtime)
        
        # Build document
        document = {
            'id': doc_id,
            'title': content_data['title'],
            'content': content_data['content'][:5000],  # Limit content size
            'excerpt': content_data['excerpt'],
            'type': 'documentation',
            'slug': slug,
            'tags': content_data.get('tags', ['documentation', 'sphinx']),
            'date_timestamp': timestamp,
            'category': 'Documentation',
            'keywords': [],  # Could extract from meta tags if available
        }
        
        # Add optional fields if they exist
        if content_data.get('metaDescription'):
            document['metaDescription'] = content_data['metaDescription']
            
        return document
    
    def index_documents(self):
        """Main indexing process"""
        print("Starting Sphinx documentation indexing...")
        
        # Get all HTML files
        html_files = self.get_html_files()
        print(f"Found {len(html_files)} HTML files to index")
        
        if not html_files:
            print("No files to index. Make sure to build the documentation first.")
            return
        
        documents = []
        errors = []
        
        for file_path in html_files:
            try:
                # Read HTML file
                with open(file_path, 'r', encoding='utf-8') as f:
                    html_content = f.read()
                
                # Extract content
                content_data = self.extract_text_from_html(html_content)
                if not content_data:
                    print(f"  Skipping {file_path} - no content found")
                    continue
                
                # Create document
                document = self.create_document(file_path, content_data)
                documents.append(document)
                
                print(f"  ✓ Processed: {document['id']}")
                
            except Exception as e:
                error_msg = f"  ✗ Error processing {file_path}: {str(e)}"
                print(error_msg)
                errors.append(error_msg)
        
        # Index documents in batches
        if documents:
            print(f"\nIndexing {len(documents)} documents to Typesense...")
            
            try:
                # Import documents with upsert action
                result = self.client.collections[self.collection_name].documents.import_(
                    documents, 
                    {'action': 'upsert'}
                )
                
                # Check results
                success_count = sum(1 for r in result if r.get('success', False))
                print(f"✓ Successfully indexed {success_count}/{len(documents)} documents")
                
                # Show any errors
                for r in result:
                    if not r.get('success', False):
                        print(f"  Error: {r.get('error', 'Unknown error')}")
                        
            except Exception as e:
                print(f"✗ Error indexing documents: {str(e)}")
                return
        
        # Summary
        print("\n" + "="*50)
        print("Indexing Summary:")
        print(f"  Total files found: {len(html_files)}")
        print(f"  Documents indexed: {len(documents)}")
        print(f"  Errors: {len(errors)}")
        
        if errors:
            print("\nErrors encountered:")
            for error in errors[:5]:  # Show first 5 errors
                print(f"  {error}")

def main():
    """Main entry point"""
    indexer = SphinxTypesenseIndexer()
    
    # Check if we can connect to Typesense
    try:
        # Try to retrieve collection info
        collection_info = indexer.client.collections[indexer.collection_name].retrieve()
        print(f"Connected to Typesense collection: {collection_info['name']}")
        print(f"Collection has {collection_info['num_documents']} existing documents\n")
    except Exception as e:
        print(f"Error connecting to Typesense: {str(e)}")
        print("Please check your credentials in .env.typesense")
        sys.exit(1)
    
    # Run indexing
    indexer.index_documents()

if __name__ == "__main__":
    main()