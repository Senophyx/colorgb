class styles:
    UNDERLINE = "\u001b[4m"
    BOLD = "\u001b[1m"
    RESET = "033[0m"

def style(text=None, style=None, reset=True) -> str:
    """
    Style. Styling the font.
    -
    -----
    List :
    - `underline`
    - `bold`
    """
    if style == "underline":
        if reset == False:
            styled = f"{styles.UNDERLINE}{text}"
        else:
            styled = f"{styles.UNDERLINE}{text}{styles.RESET}"
        
    if style == "bold":
        if reset == False:
            styled = f"{styles.BOLD}{text}"
        else:
            styled = f"{styles.BOLD}{text}{styles.RESET}"

    else:
        raise TypeError("Unknow style!")
    
    return styled
