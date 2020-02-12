.PHONY: test
test: testcov
	@pytest ./tests -vv

.PHONY: testcov
testcov:
	@pytest --cov=picpay tests/

.PHONY: format
format:
	@black picpay/

.PHONY: check
check:
	@black --check picpay/
	@flake8 picpay/

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