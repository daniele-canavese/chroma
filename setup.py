"""Setup file."""

from os.path import abspath, dirname, join

from setuptools import find_packages, setup

cwd = dirname(abspath(__file__))
with open(join(cwd, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="chroma",
    version="0.1",
    packages=find_packages(),
    python_requires=">=3.12",
    install_requires=[
        "rich>=13.7.1",
    ],
    package_dir={"chroma": "chroma"},
    url="https://github.com/daniele-canavese/chroma",
    license="APL",
    author="Daniele Canavese",
    author_email="daniele.canavese@irit.fr",
    description="pretty printing for Python",
    long_description=long_description,
)
