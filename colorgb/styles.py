from .dictionary import styles
from .errors import *

def style(text:str, style:str, reset=True):
    """
    Style. Styling the font.
    -
    -----
    Parameters :
    - text: `str`
    - style: `str`
    - reset: `True/False` | Default : `True`
    -----
    Style List :
    - `bold`
    - `italic` (Not widely supported)
    - `underline`
    - `reverse` (Swap foreground and background colors)
    - `hidden`
    - `overlined` (Not supported in Terminal app)
    """
    
    try:
        text = str(text)
        if reset == False:
            return str(styles[style]+text)
        else:
            return str(styles[style]+text+styles['reset'])
    except KeyError as error:
        raise UnknownColor(error)
