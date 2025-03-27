<h1 align="center">
  <img src="images/chroma.svg" alt="logo" style="width: 50%;"/>
</h1>
<div align="center">

# `chroma`

*Pretty printing for Python.*

[![dani](https://img.shields.io/badge/Daniele-Canavese-5822C2?logo=linkedin&&labelColor=FFC107&style=for-the-badge)](https://www.linkedin.com/in/daniele-canavese/)

[![python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![python](https://img.shields.io/badge/Poetry-60A5FA?logo=poetry&logoColor=white)](https://python-poetry.org/)
[![python](https://img.shields.io/badge/Rich-FAE742?logo=rich&logoColor=black)](https://github.com/Textualize/rich/)

[Overview](#-overview) •
[Installation and removal](#-installation-and-removal) •
[Quick start](#-quick-start) •
[References](#-references)

</div>

## 🗺️ Overview

`chroma` is a Python package for pretty printing various data with a built-in
support for colors and emojis. It is actually a wrapper around `rich` [1], a
pretty printing library.

In particular, it allows you to:

- pretty print text messages with automatic highlighting of many data types such
  as number, strings and URLs;
- select a severity level to accentuate important information;
- nicely format tables where individual rows can be emphasized;
- use progress bars with automatic ETAs.

## 🚧 Installation and removal

`chroma` makes use of `poetry` to install its dependencies. If you are using a Debian-like OS you can install them via
the following commands:

```shell
sudo apt install python3 pipx
pipx install poetry
poetry self add poetry-plugin-shell # Optional, but useful.
```

### I want to use it as a package

If you want to use `chroma` as a package in a `poetry`-managed project , you can install it with the following command:

```shell
poetry add git+https://github.com/daniele-canavese/chroma.git
```

Conversely, `chroma` can be uninstalled with:

```shell
poetry remove chroma
```

### I want to develop it

To create an environment for developing `chroma`, just run the command:

```shell
poetry install
```

To test `chroma` you can also launch all the test cases with:

```shell
poetry run pytest
```

Instead, to completely remove the development environment, execute:

```shell
poetry env remove --all
```

## 🔥 Quick start

The most important function in `chroma` is `pprint`, which is used to pretty
print anything and can be used as a substitute to the traditional
Python's `print`.

The `Table` class instances represent tabular data and can be fed to `pprint` as
well. In addition, the `ProgressBar` class is an iterable that automatically
display a progress bar.

The `examples` folder contains many commented usage examples; in particular:

- `examples/printing.py` shows how to pretty print various text messages;
- `examples/progress.py` contains some progress bar instances;
- `examples/table.py` presents different ways of printing tables.

## 📚️ References

- [1] [`rich`](https://github.com/Textualize/rich)
