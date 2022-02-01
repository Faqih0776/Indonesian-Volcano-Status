@echo off
rmdir build dist /S /Q
py -m build
py -m twine upload --repository pypi dist/*