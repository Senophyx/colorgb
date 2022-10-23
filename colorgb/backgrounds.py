from .dictionary import background
from .errors import *

def bg(text:str, color:str, reset=True):
    """
    Backgrounds. The color will appear behind the text.
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
            return str(background[color]+text)
        else:
            return str(background[color]+text+background['reset'])
    except KeyError as error:
        raise UnknownColor(error)
