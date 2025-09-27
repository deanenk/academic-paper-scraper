import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from orchestrator import PaperScraper
from schemas import SearchQuery

def test_different_sources():
    print("🧪 Testing different data sources...")
    
    queries = [
        "artificial intelligence",
        "quantum computing", 
        "bioinformatics"
    ]
    
    for query_str in queries:
        print(f"\nTesting query: {query_str}")
        query = SearchQuery(query=query_str, max_results=3)
        scraper = PaperScraper()
        results = scraper.execute_query(query)
        print(f"Results for {query_str}: {results}")

if __name__ == "__main__":
    test_different_sources()