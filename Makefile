BLUE='\033[0;34m'
NC='\033[0m'

test:
	@pytest

lint:
	@echo "\n${BLUE}Running Pylint against source and test files...${NC}\n"
	@pylint --rcfile=setup.cfg *.py
	@echo "\n${BLUE}Running Flake8 against source and test files...${NC}\n"
	@flake8

clean:
	rm -rf .pytest_cache .coverage .pytest_cache

veryclean: clean
	find . | grep -E "(__pycache__|\.pyc|\.pyo)" | xargs rm -rf

.PHONY: clean test lint
