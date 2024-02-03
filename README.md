<h1 style="text-align: center;">
  <img src="images/chroma.svg" alt="logo" style="max-width: 50%;"/>
</h1>
<div style="text-align: center;">

# `chroma`

**Pretty printing for Python.**

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
support for colors and emojis.

In particular, it allows you to:

- nicely format tables where individual rows can be emphasized;
- pretty print text messages with automatic highlighting of many data types such
  as number, strings and URLs;
- select a severity level to accentuate important information;
- use progress bars with automatic ETAs.

## Installation and removal

`chroma` can be easily installed via `pipenv` with the following command:

```shell
pipenv install -e git+https://github.com/daniele-canavese/chroma.git#egg=chroma
```

Conversely, it can be uninstalled with:

```shell
pipenv uninstall chroma
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
