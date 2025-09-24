# Create a test script test_storage.py
from src.agents.storage_agent import StorageAgent
from src.schemas import SearchQuery

storage = StorageAgent()
test_data = [{
    "title": "Test Paper",
    "authors": ["Author One", "Author Two"],
    "abstract": "Test abstract"
}]

mock_query = SearchQuery(query="test", sources=["IEEE"], max_results=10)

# Use the correct method based on which option you choose
filename = storage.save_results(test_data, mock_query)
print(f"Saved to: {filename}")