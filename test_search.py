# Create a test script test_search.py
from src.agents.search_agent import SearchAgent
from src.schemas import SearchQuery
from src.agents.rate_limiter import RateLimiter

search_agent = SearchAgent()
rate_limiter = RateLimiter(requests_per_minute=10)

# Fix: Use 'query' instead of 'keywords'
query = SearchQuery(query="machine learning", sources=["arXiv"], max_results=5)

urls = search_agent.search(query, rate_limiter)
print(f"Found URLs: {urls}")