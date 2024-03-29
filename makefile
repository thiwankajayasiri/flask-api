ifeq (, $(shell which poetry))
$(error "No poetry in $(PATH), consider installing it from https://python-poetry.org/docs/#installation")
endif

install:
	poetry install

test:
	poetry run pytest

coverage:
	poetry run pytest --cov=./ --cov-report=xml:./coverage.xml

doc:
	poetry run pdoc ./app.py -o ./docs

run:
	poetry run flask run

.PHONY: install test coverage doc run