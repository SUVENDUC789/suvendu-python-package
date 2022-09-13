# suvendu-python-package
### 1. Create setup.py and write some code :
```python
from setuptools import setup, find_packages, find_namespace_packages

d = '''In the same way, a package in Python takes the concept of the modular approach to next logical level. As you know, a module can contain multiple objects, such as classes, functions, etc. A package can contain one or more relevant modules. Physically, a package is actually a folder containing one or more module files.'''


setup(
name='suvendu', 
version='1.1.1',
description='Suvendu Chowdhury create this python package | Also I am a student and an enthusiastic techie.', 
long_description=d,
author='Suvendu Chowdhury',
packages=['suvendu'],
install_requires=[],
)

```

### 2. After run this command YourPackage_versionX.X.X.whl file is ready:
```terminal
python setup.py sdist bdist_wheel
```

### 3. Install wheel file globally in your system:
```terminal
pip install suvendu-1.1.1-py3-none-any.whl
```
### 4. Uninstall Python-Package  globally in your system:
```terminal
pip uninstall suvendu
```
