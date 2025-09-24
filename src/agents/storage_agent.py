# storage_agent.py
import json
import os
from datetime import datetime

class StorageAgent:
    def __init__(self):
        # Create results directory if it doesn't exist
        self.results_dir = "results"
        os.makedirs(self.results_dir, exist_ok=True)
    
    def store_paper(self, paper_data):
        # Implement paper storage logic here
        # This could save to database, file system, etc.
        pass
    
    def retrieve_paper(self, paper_id):
        # Implement paper retrieval logic here
        pass
    
    def save_results(self, papers_data, search_query):
        """Save multiple papers from a search query to a JSON file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"search_results_{search_query.query.replace(' ', '_')}_{timestamp}.json"
        filepath = os.path.join(self.results_dir, filename)
        
        results = {
            "query": search_query.query,
            "sources": search_query.sources,
            "max_results": search_query.max_results,
            "timestamp": timestamp,
            "papers": papers_data
        }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        
        return filepath