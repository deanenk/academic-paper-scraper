import os
import sys

def create_project_structure(base_path):
    """
    Creates the project structure for the academic paper scraper.
    """
    # Define the directory structure
    structure = {
        'src': {
            '__init__.py': '',
            'schemas.py': '# For SearchQuery class\n',
            'orchestrator.py': '# PaperScraperOrchestrator\n',
            'agents': {
                '__init__.py': '',
                'search_agent.py': '# SearchAgent & Parser classes\n',
                'extraction_agent.py': '# ExtractionAgent & Extractor classes\n',
                'storage_agent.py': '# StorageAgent\n'
            }
        },
        'tests': {
            '__init__.py': '',
            'test_search_agent.py': '# Unit tests for SearchAgent\n',
            'test_extraction_agent.py': '# Unit tests for ExtractionAgent\n',
            'test_data': {}  # Empty directory for mock HTML files
        },
        'output': {},  # Empty directory for scraped results
        'requirements.txt': '# Python dependencies\nrequests\nbeautifulsoup4\nlxml\n',
        'main.py': '# Main script to run everything\n',
        'README.md': '# Academic Paper Scraper\n\nA system to scrape metadata for academic papers from sources like IEEE, ACM, and arXiv.\n'
    }

    def create_directory(path, contents):
        """Recursively create directories and files"""
        for name, content in contents.items():
            full_path = os.path.join(path, name)
            if isinstance(content, dict):
                # It's a directory
                os.makedirs(full_path, exist_ok=True)
                print(f"Created directory: {full_path}")
                create_directory(full_path, content)
            else:
                # It's a file
                if not os.path.exists(full_path):
                    with open(full_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Created file: {full_path}")
                else:
                    print(f"File already exists: {full_path}")

    # Create the structure
    os.makedirs(base_path, exist_ok=True)
    print(f"Creating project structure in: {base_path}")
    create_directory(base_path, structure)
    print("Project structure created successfully!")

if __name__ == "__main__":
    # Determine the target directory
    if len(sys.argv) > 1:
        target_dir = sys.argv[1]
    else:
        # Default to current directory if none specified
        target_dir = os.getcwd()
    
    create_project_structure(target_dir)
