# helper modules
import sys
from io import StringIO


def set_stdio(inp):
    """Redirect stdio to use string buffer."""
    default_stdin = sys.stdin
    sys.stdin = StringIO(inp)
    default_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    return default_stdin, default_stdout, mystdout

def reset_stdio(default_stdout, default_stdin):
    """Reset stdio to defaults."""
    sys.stdin = default_stdin
    sys.stdout = default_stdout

def run(function, inp):
    """Common helper function for running tests."""
    sys.argv = inp.split()  # input by command line parameters
    default_stdin, default_stdout, mystdout = set_stdio(inp)    # input by input()
    function()
    reset_stdio(default_stdin, default_stdout)
    out = mystdout.getvalue()[:-1]  # ignore the final newline
    return out
