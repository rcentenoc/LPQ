
# Lenguaje de programación Q

Source code for the Interpreters course at Q.

# Install dependencies

1. Create a virtual environment:
```bash
python3.11 -m venv LpqVenv
```

2. Activate the virtual environment:
```bash
source LpqVenv/Scripts/activate
```

3. Install dependencies
```bash
pip install nose2
pip install mypy
```

# Run type checker and test suite

To run the type checker and and the test suite run the following command from
the root directory.

```bash
mypy .
nose2
```

# Run the interpreter
```bash
python3.11 main.py
```
