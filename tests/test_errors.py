import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from orchestrator import PaperScraper
from schemas import SearchQuery

def test_error_handling():
    print("🧪 Testing error handling...")
    
    # Test empty query
    try:
        query = SearchQuery(query="", max_results=2)
        scraper = PaperScraper()
        results = scraper.execute_query(query)
        print("❌ Empty query should have failed")
    except Exception as e:
        print("✅ Empty query failed as expected:", str(e)[:100])
    
    # Test invalid query
    try:
        query = SearchQuery(query=None, max_results=2)
        scraper = PaperScraper()
        results = scraper.execute_query(query)
        print("❌ Invalid query should have failed")
    except Exception as e:
        print("✅ Invalid query failed as expected:", str(e)[:100])

if __name__ == "__main__":
    test_error_handling()