import os
import inspect

SUBMIT_PIPE = "{0}/submit".format(os.environ['SCAVENGERDATADIR'])

# Styles
BOLD = 1
UDL = 2  # Underline
REV = 4  # Reversed foreground/background color
BLUE = 8
RED = 16
MAG = 32 # Magenta

class UnimplementedError(Exception):
    def __init__(self):
        self.value = inspect.stack()[1][3]
    def __str__(self):
        return "function {0} is UNIMPLEMENTED".format(repr(self.value))

# Compose different styles through the '+' operator
#
# For bold and blue text, pass in style=BOLD+BLUE
def text(message, style=BOLD):
    normal = '\033[0m'

    bold = '\033[1m'
    underline = '\033[4m'
    reverse = '\033[7m'

    red = '\033[31m'
    blue = '\033[34m'
    magenta = '\033[35m'

    delimiter = ''
    if style & BOLD == BOLD:
        delimiter += bold
    if style & UDL == UDL:
        delimiter += underline
    if style & REV == REV:
        delimiter += reverse
    if style & RED == RED:
        delimiter += red
    if style & BLUE == BLUE:
        delimiter += blue 
    if style & MAG == MAG:
        delimiter += magenta
    return "{0}{1}{2}".format(delimiter, message, normal)

def announce(message, style=BOLD):
    print(text("\n{0}\n".format(message), style))

# Check if the class attribute is defined
#
# To check if "self.attribute" is defined, pass in (self, "attribute")
def attr_defined(self, var):
    try:
        eval("self.{0}".format(var))
    except AttributeError:
        return False
    else:
        return True
