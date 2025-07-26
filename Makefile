# Makefile for mr-millionaire packaging and deployment

PACKAGE_NAME = mr_millionaire
PYPI_REPO = pypi  
VERSION = 0.1.1

.PHONY: all clean build upload test lint format help

all: build

help:
	@echo "Usage: make [target]"
	@echo "Targets:"
	@echo "  clean     - Remove build artifacts"
	@echo "  build     - Build the package (wheel + sdist)"
	@echo "  upload    - Upload to PyPI via Twine"
	@echo "  test      - Run tests with pytest"
	@echo "  lint      - Run ruff linter"
	@echo "  format    - Format code with ruff"
	@echo "  all       - Build everything (default)"

clean:
	rm -rf dist/ build/ src/mr_millionaire.egg-info

build:clean
	python -m build

upload:
	twine upload dist/*

test:
	pytest

lint:
	ruff check src/

format:
	ruff format src/
