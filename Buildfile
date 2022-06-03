@function clean:
rm -rf dist
rm -rf ports.py.egg-info


\endfunc

@function build:
@q python -m pip install --upgrade build
@q python -m pip install --upgrade twine
@q python -m build
python3 -m twine upload --repository pypi dist/*
\endfunc

@function clean2:
rm -rf dist
rm -rf ports.py.egg-info
\endfunc
