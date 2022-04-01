SHELL := bash
.ONESHELL:

.PHONY: help \
> setup \
> clean \
> lint_staged \
> lint_all


setup:
	@echo installing python dependencies

	pipenv install         --skip-lock
	pipenv install --dev   --skip-lock
	pipenv install .
	pre-commit install
	pre-commit autoupdate

clean:
	echo 'Removing cache files'
	@rm -rf *.egg-info *.log
	@rm -rf build/ dist/

pipable:
	@python setup.py check
	@python setup.py sdist
	@python setup.py bdist_wheel --universal
