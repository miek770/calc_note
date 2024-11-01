# Calculation Note

`calc_note` is a collection of utilities to ease the production of professional calculation notes using [Python](https://www.python.org/) and [Jupyter](https://jupyter.org/).

## Installation

Using [pip](https://pip.pypa.io/en/stable/):

`pip install calc_note`

## Usage

Import `calc_note` with:

```python
from calc_note.display import *
```

See [tests/tests_calc_note.ipynb](tests/test_calc_note.ipynb) for usage examples.

### show(pd.DataFrame)

Calling `show()` in a notebook on a [DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html) (instead of simply calling the [DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)) prints a table that will remain pretty after the notebook's conversion to PDF.

### md(str)

`calc_notes` imports the following:

```python
from IPython.display import Markdown as md
```

The `md(str)` function can thus be used to generate [Markdown](https://en.wikipedia.org/wiki/Markdown) content from a [Python](https://www.python.org/) cell. The latter is useful to embed variables in [Markdown](https://en.wikipedia.org/wiki/Markdown) tables, for example.

### %%render Cell Magic

The `%%render` cell magic from [handcalcs](https://github.com/connorferster/handcalcs) is include to render code blocks as [LaTeX](https://www.latex-project.org/).

## Contributing

Contributions are welcome. The package is managed with [poetry](https://python-poetry.org/) starting from v0.3.0. A few useful commands are defined in [Makefile](Makefile).