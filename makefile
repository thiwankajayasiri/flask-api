# Check if poetry is installed
ifeq (, $(shell which poetry))
$(error "No poetry in $(PATH), consider installing it from https://python-poetry.org/docs/#installation")
endif

install:
	poetry install

test:
	poetry run pytest

run:
	poetry run flask run

.PHONY: install test run