import sys

def running_in_notebook_or_ipython():
    """
    Returns ``True`` if the module is running in IPython kernel,
    ``False`` if in IPython shell or other Python shell.
    """
    return "ipykernel" in sys.modules

# TODO: Aaron to add his first unit-test
#
# ## Starting references:
# * https://en.wikipedia.org/wiki/Unit_testing
# * https://the-turing-way.netlify.app/reproducible-research/testing/testing-unittest.html