from .dictionary import fg
from .errors import *

def fore(text:str, color:str, reset=True):
    """
    Fore. The color will appear in the text.
    -
    -----
    Parameters :
    - text: `str`
    - color: `str`
    - reset: `True/False` | Default: `True`
    -----
    Normal Colors :
    - `black`
    - `red`
    - `green`
    - `yellow`
    - `blue`
    - `purple`
    - `cyan`
    - `white`
    -----
    Light Colors :
    - `grey`
    - `lred`
    - `lgreen`
    - `lyellow`
    - `lblue`
    - `lpurple`
    - `lcyan`
    """

    try:
        text = str(text)
        if reset == False:
            return str(fg[color]+text)
        else:
            return str(fg[color]+text+fg['reset'])
    except KeyError as error:
        raise UnknownColor(error)
