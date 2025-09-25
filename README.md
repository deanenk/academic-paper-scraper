# Academic Paper Scraper

A Python tool for scraping academic papers from various sources including IEEE, ArXiv, and more.

## Features
- Search for academic papers by keyword
- Extract metadata (title, authors, abstract, etc.)
- Download PDFs (when available)
- Export results to CSV/JSON

## Installation
```bash
git clone https://github.com/deanenk/academic-paper-scraper.git
cd academic-paper-scraper
pip install -r requirements.txt

##Usage
python
from scraper.orchestrator import PaperScraper

scraper = PaperScraper()
results = scraper.search("machine learning")
Project Structure
text
academic-paper-scraper/
├── src/
├── tests/
├── data/
├── requirements.txt
└── README.md
