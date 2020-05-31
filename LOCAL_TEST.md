
for local tests create a new env in the root project named venv

```
python -m venv venv
```

activate the virtual env

install the package

```
pip install -e .
```

write test code in testscript.py

after package change run

```
pip install -e . --upgrade
```