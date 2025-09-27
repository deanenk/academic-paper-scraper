import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from orchestrator import PaperScraper
from schemas import SearchQuery

def test_data_quality():
    print("🧪 Testing data quality...")
    
    query = SearchQuery(query="machine learning", max_results=3)
    scraper = PaperScraper()
    results = scraper.execute_query(query)
    
    # Check if we got the expected keys in the results
    expected_keys = ['query', 'urls_found', 'papers_parsed', 'storage_path']
    if all(key in results for key in expected_keys):
        print("✅ Data structure test PASSED")
    else:
        print("❌ Data structure test FAILED")
        print(f"Expected keys: {expected_keys}")
        print(f"Actual keys: {list(results.keys())}")
    
    # Check if the numbers make sense
    if results['papers_parsed'] <= results['urls_found']:
        print("✅ Data consistency test PASSED")
    else:
        print("❌ Data consistency test FAILED")
        print(f"Papers parsed: {results['papers_parsed']}, URLs found: {results['urls_found']}")

if __name__ == "__main__":
    test_data_quality()