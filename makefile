.PHONY: test
test: testcov
	@pytest ./tests -vv

.PHONY: testcov
testcov:
	@pytest --cov=python_picpay tests/

.PHONY: format
format:
	@black python_picpay/

.PHONY: check
check:
	@black --check python_picpay/
	@flake8 python_picpay/

.PHONY: clean-pyc clean-build clean
clean: clean-build clean-pyc

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info
	rm -fr *.egg

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +