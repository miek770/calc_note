import pandas as pd
from IPython.display import display
from IPython.display import Markdown as md


# Pretty DataFrame output in Markdown (makes it possible for LaTeX to convert it to a
# pretty table afterwards)
# ===================================================================================


def show(df):
    """Show pretty DataFrames in PDF conversion:
    https://stackoverflow.com/questions/20685635/pandas-dataframe-as-latex-or-html-table-nbconvert
    """
    display(md(df.to_markdown()))


# Pretty Markdown table output in LaTeX
# -------------------------------------

pd.set_option("display.notebook_repr_html", True)


def _repr_latex_(self):
    """This bit is important to get a pretty Dataframe output in LaTex:
    https://stackoverflow.com/questions/20685635/pandas-dataframe-as-latex-or-html-table-nbconvert
    """
    return "\centering{%s}" % self.to_latex()
