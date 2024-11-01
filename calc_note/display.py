import pandas as pd
from IPython.display import display
from IPython.display import Markdown as md

# To provide the %%render cell magic
# See: https://github.com/connorferster/handcalcs
import handcalcs.render


def show(df):
    """Show pretty DataFrames in PDF conversion:
    https://stackoverflow.com/questions/20685635/pandas-dataframe-as-latex-or-html-table-nbconvert
    """
    display(md(df.to_markdown()))


# Pretty Markdown table output in LaTeX
pd.set_option("display.notebook_repr_html", True)


def _repr_latex_(self):
    """This bit is important to get a pretty Dataframe output in LaTex:
    https://stackoverflow.com/questions/20685635/pandas-dataframe-as-latex-or-html-table-nbconvert
    """
    return r"\centering{%s}" % self.to_latex()
