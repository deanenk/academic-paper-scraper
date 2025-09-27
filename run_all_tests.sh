#!/bin/bash
echo "Running all tests..."
python tests/test_basic.py
python tests/test_errors.py
python tests/test_sources.py
python tests/test_performance.py
python tests/test_data_quality.py
echo "All tests completed!"
