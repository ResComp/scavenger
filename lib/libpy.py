import os

SUBMIT_PIPE = "{0}/submit".format(os.environ['DATADIR'])

# Styles
BOLD=0
BLUE=1
RED=2

# Valid styles: bold, red, blue
def text(message, style=BOLD):
    bold = '\033[1m'
    normal = '\033[0m'
    blue = '\033[94m'
    red = '\033[91m'

    delimiter = bold
    if style == BLUE:
        delimiter += blue
    if style == RED:
        delimiter += red
    print("{0}{1}{2}".format(delimiter, message, normal))

def announce(message, style=BOLD):
    text("\n{0}\n".format(message), style)
