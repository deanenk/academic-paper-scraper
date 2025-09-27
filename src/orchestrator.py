# orchestrator.py
from schemas import SearchQuery
from agents.search_agent import SearchAgent
from agents.parser_agent import ParserAgent
from agents.storage_agent import StorageAgent
from agents.rate_limiter import RateLimiter

class PaperScraper:
    def __init__(self):
        self.search_agent = SearchAgent()
        self.parser_agent = ParserAgent()
        self.storage_agent = StorageAgent()
        self.rate_limiter = RateLimiter(requests_per_minute=10)
    
    def execute_query(self, query: SearchQuery):
        """
        Execute a complete search, parse, and store workflow
        """
        print(f"Executing query: {query.query}")
        
        # Step 1: Search for papers
        print("Step 1: Searching for papers...")
        urls = self.search_agent.search(query, self.rate_limiter)
        print(f"Found {len(urls)} URLs")
        
        # Step 2: Parse paper details from URLs
        print("Step 2: Parsing paper details...")
        papers = []
        for url in urls:
            paper_data = self.parser_agent.parse(url, self.rate_limiter)
            if paper_data:
                papers.append(paper_data)
        
        # Step 3: Store the results
        print("Step 3: Storing results...")
        if papers:
            filename = self.storage_agent.save_results(papers, query)
            print(f"Results saved to: {filename}")
        else:
            filename = "No papers found to save"
        
        return {
            "query": query.query,
            "urls_found": len(urls),
            "papers_parsed": len(papers),
            "storage_path": filename
        }