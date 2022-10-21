"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path
import os
import sys
here = path.abspath(path.dirname(__file__))

requires = [
    'pygame',
    'numpy'
]

if sys.argv[-1] == "publish":  # requests
    os.system("python setup.py sdist")  # bdist_wheel
    os.system("twine upload dist/* --skip-existing")
    sys.exit()

# Following the PyPa solution for Single-sourcing the package version:
# https://packaging.python.org/en/latest/guides/single-sourcing-package-version/
def read(rel_path: str) -> str:
    with open(os.path.join(here, rel_path)) as fp:
        return fp.read()

def get_version(rel_path: str) -> str:
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")


# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="hooman",  # Required
    version=get_version(path.join("hooman", "__init__.py")),  # Required
    description="Pygame for humans",  # Optional
    long_description=long_description,  # Optional
    long_description_content_type="text/markdown",  # Optional (see note above)
    url="https://github.com/Abdur-RahmaanJ/hooman",  # Optional
    author="Abdur-Rahmaan Janhangeer",  # Optional
    author_email="arj.python@gmail.com",  # Optional
    # Classifiers help users find your project by categorizing it.
    #
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        # 'Topic :: Weather',
        # Pick your license as you wish
        "License :: OSI Approved :: MIT License",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        # These classifiers are *not* checked by 'pip install'. See instead
        # 'python_requires' below.
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="human pygame canvas api wrapper game processing",  # Optional
    # You can just specify package directories manually here if your project is
    # simple. Or you can use find_packages().
    #
    # Alternatively, if you just want to distribute a single Python file, use
    # the `py_modules` argument instead as follows, which will expect a file
    # called `my_module.py` to exist:
    #
    #   py_modules=["my_module"],
    #
    # packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # Required
    packages=["hooman"],
    include_package_data=True,
    python_requires=">=3.4",
    install_requires=requires,  # Optional
    project_urls={  # Optional
        "Bug Reports": "https://github.com/Abdur-RahmaanJ/hooman/issues",
        "Source": "https://github.com/Abdur-RahmaanJ/hooman/",
    },
    entry_points={"console_scripts": ["hooman=hooman.__main__:main"]},
)
