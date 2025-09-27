import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from orchestrator import PaperScraper
from schemas import SearchQuery

def test_basic_functionality():
    print("🧪 Testing basic functionality...")
    
    try:
        # Create a SearchQuery object (NOT passed to PaperScraper constructor)
        query = SearchQuery(
            query="machine learning",
            max_results=2
        )
        
        # Initialize the scraper (no parameters)
        scraper = PaperScraper()
        
        # Execute the query
        results = scraper.execute_query(query)
        
        print(f"📊 Results: {results}")
        
        if results and results['papers_parsed'] > 0:
            print("✅ Basic functionality test PASSED")
            print(f"📄 Number of papers parsed: {results['papers_parsed']}")
            print(f"💾 Saved to: {results['storage_path']}")
        else:
            print("❌ No results returned or no papers parsed")
            
    except Exception as e:
        print(f"❌ Error during test: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_basic_functionality()