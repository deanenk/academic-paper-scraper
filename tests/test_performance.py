import sys
import os
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from orchestrator import PaperScraper
from schemas import SearchQuery

def test_performance():
    print("🧪 Testing performance...")
    
    start_time = time.time()
    
    queries = [
        "deep learning",
        "natural language processing", 
        "computer vision"
    ]
    
    for query_str in queries:
        query = SearchQuery(query=query_str, max_results=5)
        scraper = PaperScraper()
        results = scraper.execute_query(query)
        print(f"Query: {query_str} - Papers parsed: {results['papers_parsed']}")
    
    end_time = time.time()
    duration = end_time - start_time
    print(f"⏱️ Total time: {duration:.2f} seconds")
    
    if duration < 120:  # Less than 2 minutes
        print("✅ Performance test PASSED")
    else:
        print("❌ Performance test FAILED - Too slow")

if __name__ == "__main__":
    test_performance()