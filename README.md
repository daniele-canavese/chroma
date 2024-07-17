<h1 align="center">
  <img src="images/chroma.svg" alt="logo" style="width: 50%;"/>
</h1>
<div align="center">

# `chroma`

*Pretty printing for Python.*

[![dani](https://img.shields.io/badge/Daniele-Canavese-5822C2?logo=linkedin&&labelColor=0A66C2)](https://www.linkedin.com/in/daniele-canavese/)
&nbsp;
[![python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
&nbsp;
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/3e8c7f470efe44e89268424c5ad6467b)](https://app.codacy.com?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)

[Overview](#overview) •
[Installation and removal](#installation-and-removal) •
[Getting started](#getting-started)

</div>

## Overview

`chroma` is a Python package for pretty printing various data with a built-in
support for colors and emojis. It is actually a wrapper around `rich` [1], a
pretty printing library.

In particular, it allows you to:

- nicely format tables where individual rows can be emphasized;
- pretty print text messages with automatic highlighting of many data types such
  as number, strings and URLs;
- select a severity level to accentuate important information;
- use progress bars with automatic ETAs.

## Installation and removal

`chroma` can be easily installed via `conda` (or `pipenv`).

### Development environment

If you want to create an environment for developing `chroma`, just run the command:

```shell
conda env create --file environment.yml
```

And to remove this environment launch:

```shell
conda remove --name chroma --all
```

### Adding a dependency

If, instead, you want to use `chroma` in one of your projects, just add the following dependencies in your `conda`'s `environment.yaml`:

```
  - pip
  - pip:
      - "--editable=git+https://ACCESS_TOKEN@github.com/daniele-canavese/chroma.git#egg=chroma"
```

Where `ACCESS_TOKEN` is you GitHub's access token.

Conversely, `chroma` can be uninstalled with:

```shell
conda uninstall chroma
```

## Getting started

The most important function in `chroma` is `pprint`, which is used to pretty
print anything. The `Table` instances
obviously represent tabular data and can be fed to `pprint` as well. In
addition, the `ProgressBar` class is an iterable
that automatically display a progress bar.

The `examples` folder contains many commented usage examples of `chroma`. In
particular:

- `examples/printing.py` shows how to pretty print various text messages;
- `examples/progress.py` contains some progress bar instances;
- `examples/table.py` presents different ways of printing tables.

## References

[1] [`rich`](https://github.com/Textualize/rich), a Python library for rich text
and beautiful formatting in the terminal.
