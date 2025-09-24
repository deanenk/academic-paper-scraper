# Create a test script test_integration.py
from src.orchestrator import PaperScraperOrchestrator
from src.schemas import SearchQuery

orchestrator = PaperScraperOrchestrator()
query = SearchQuery(
    query="machine learning",  # Fix: use 'query' instead of 'keywords'
    sources=["arXiv"],  # Start with just one source
    max_results=3  # Keep it small for testing
)

result = orchestrator.execute_query(query)
print(f"Result: {result}")