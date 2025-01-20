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
[Getting started](#-getting-started) •
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

## 🏗️ Installation and removal

`chroma` is managed via `poetry`.

### Usage

`chroma` version `🅇.🅈.🅉-🄱` can be installed in a `poetry` environment with the
following command:

```shell
poetry add https://github.com/daniele-canavese/chroma.git
```

Conversely, `chroma` can be uninstalled with:

```shell
conda remove chroma
```

### Development

To create an environment for developing `chroma`, just run the command:

```shell
poetry install
poetry shell
```

To remove all the development environments, execute:

```shell
poetry env remove --all
```

## 🧭 Getting started

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

## 🗂️️ References

[1] [`rich`](https://github.com/Textualize/rich), a Python library for rich text
and beautiful formatting in the terminal
