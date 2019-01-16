default: test

clean: clean-build clean-pyc

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

init:
	pipenv install

init-dev:
	pipenv install -d

run-test:
	pipenv run pytest --flake8 --black --cov=chroniker --cov-report term-missing tests/

release: clean
	pipenv run twine upload

run: init run-app
r: run-app
test: init-dev run-test
t: run-test
