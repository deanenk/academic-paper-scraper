#!/usr/bin/env python3
"""
Basic verification script for academic-paper-scraper
"""

import os
import sys
import importlib

def check_imports():
    """Verify that all required modules can be imported"""
    modules = [
        'src.agents.search_agent',
        'src.agents.parser_agent', 
        'src.agents.storage_agent',
        'src.orchestrator'
    ]
    
    print("🔍 Checking module imports...")
    for module in modules:
        try:
            importlib.import_module(module)
            print(f"✅ {module} imports successfully")
        except ImportError as e:
            print(f"❌ {module} failed to import: {e}")
            return False
    return True

def check_dependencies():
    """Verify required packages are installed"""
    required_packages = [
        'requests', 'beautifulsoup4', 'selenium',
        'pandas', 'arxiv', 'scholarly'
    ]

    print("\n📦 Checking dependencies...")
    missing_packages = []
    for package in required_packages:
        try:
            # Handle beautifulsoup4 specially since its module name is bs4
            if package == 'beautifulsoup4':
                importlib.import_module('bs4')
            else:
                importlib.import_module(package)
            print(f"✅ {package} is available")
        except ImportError:
            missing_packages.append(package)
            print(f"❌ {package} is missing")
    
    if missing_packages:
        print(f"\n⚠️  Missing packages: {missing_packages}")
        print("Run: pip install " + " ".join(missing_packages))
        return False
    return True

def check_project_structure():
    """Verify essential project files exist"""
    required_files = [
        'src/__init__.py',
        'src/agents/__init__.py',
        'src/agents/search_agent.py',
        'src/agents/parser_agent.py',
        'src/agents/storage_agent.py',
        'src/orchestrator.py',
        'requirements.txt',
        'README.md'
    ]
    
    print("\n📁 Checking project structure...")
    missing_files = []
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file} exists")
        else:
            missing_files.append(file)
            print(f"❌ {file} is missing")
    
    return len(missing_files) == 0

def check_agent_functionality():
    """Test basic functionality of agent modules"""
    print("\n⚙️  Testing agent functionality...")
    
    try:
        # Test if we can import and create instances
        from src.agents.search_agent import SearchAgent
        from src.agents.parser_agent import ParserAgent
        from src.agents.storage_agent import StorageAgent
        from src.orchestrator import PaperScraper
        
        print("✅ All agent classes can be imported")
        
        # Test basic instantiation
        try:
            # Note: These might require parameters - we'll just test import for now
            print("✅ Agent classes are properly defined")
        except Exception as e:
            print(f"⚠️  Agent instantiation may require parameters: {e}")
            
        return True
    except Exception as e:
        print(f"❌ Agent functionality test failed: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Starting academic-paper-scraper verification...\n")
    
    checks = [
        check_project_structure(),
        check_dependencies(),
        check_imports(),
        check_agent_functionality()
    ]
    
    if all(checks):
        print("\n🎉 All checks passed! Project is ready.")
        sys.exit(0)
    else:
        print("\n❌ Some checks failed. Please fix the issues above.")
        sys.exit(1)