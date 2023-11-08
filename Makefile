.PHONY: install test clean

test:
	python -m unittest discover -s tests -p 'test_*.py'

clean:
	find . -name "*.pyc" -exec rm -f {} +
	find . -name "__pycache__" -exec rm -rf {} +