.PHONY: pypi

README.rst: README.md
	pandoc -i $< -o $@

pypi: README.rst
	python setup.py register -r pypi sdist upload -r pypi

