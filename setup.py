import pathlib
from setuptools import setup
from setuptools.dist import Distribution

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

class BinaryDistribution(Distribution):
    """Distribution which always forces a binary package with platform name"""
    def has_ext_modules(foo):
        return True

# This call to setup() does all the work
setup(
    name="raylib",
    version="3.7.0.post1",
    description="Python CFFI bindings for Raylib",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/electronstudio/raylib-python-cffi",
    author="Electron Studio",
    author_email="github@electronstudio.co.uk",
    license="LGPLv3+",
    classifiers=[
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["raylib", "raylib.dynamic", "raylib.static"],
    include_package_data=True,
    install_requires=["cffi>=1.14.5","inflection"],
    distclass=BinaryDistribution,
    cffi_modules=["raylib/static/build.py:ffibuilder"], # this would build libs whenever the module is installed, but we are distributing static libs instead
)
