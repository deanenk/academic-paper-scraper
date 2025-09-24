#!/usr/bin/env python3
"""
Main entry point for the Academic Paper Scraper
"""

import argparse
from src.orchestrator import PaperScraperOrchestrator
from src.schemas import SearchQuery

def main():
    """Main function to run the paper scraper"""
    parser = argparse.ArgumentParser(description='Academic Paper Scraper')
    parser.add_argument('--query', '-q', type=str, required=True, 
                       help='Search query (e.g., "machine learning")')
    parser.add_argument('--sources', '-s', nargs='+', default=['arXiv'],
                       help='Sources to search: arXiv, IEEE, ACM')
    parser.add_argument('--max-results', '-m', type=int, default=10,
                       help='Maximum number of results to fetch')
    
    args = parser.parse_args()
    
    # Create the search query
    query = SearchQuery(
        query=args.query,
        sources=args.sources,
        max_results=args.max_results
    )
    
    # Run the scraper
    print(f"Starting search for: {args.query}")
    print(f"Sources: {args.sources}")
    print(f"Max results: {args.max_results}")
    print("-" * 50)
    
    orchestrator = PaperScraperOrchestrator()
    result = orchestrator.execute_query(query)
    
    print("-" * 50)
    print("Search completed!")
    print(f"URLs found: {result['urls_found']}")
    print(f"Papers parsed: {result['papers_parsed']}")
    print(f"Results saved to: {result['storage_path']}")

if __name__ == "__main__":
    main()