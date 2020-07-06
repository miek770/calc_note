# Calculation Note

`calc_note` is a collection of utilities to ease the production of professional calculation notes using [Python](https://www.python.org/) and [Jupyter](https://jupyter.org/).

## Installation

### Using [pip](https://pip.pypa.io/en/stable/)

Simply run:

`pip install -U --user calc_note`

Install any missing requirement using the same method.

## Usage

`from calc_note.display import *`

Afterward, simply call `show()` in your notebook to print [DataFrames](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html) (instead of simply calling the [DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)), and `md("My content...")` to generate [Markdown](https://en.wikipedia.org/wiki/Markdown) content from a [Python](https://www.python.org/) cell. The latter is useful to embed variables in [Markdown](https://en.wikipedia.org/wiki/Markdown) tables, for example.

## Contributing

If you wish to contribute, please submit [issues](https://github.com/miek770/calc_note/issues) and [pull requests](https://github.com/miek770/calc_note/pulls) through [this repo](https://gitlab.com/miek770/energy_tools#contributing).