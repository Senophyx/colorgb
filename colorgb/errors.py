class ColorgbErrors(Exception):
    def __init__(self, message:str=None):
        if message is None:
            message = 'An unknown error has occurred within ColorGB.'
        super().__init__(message)

class UnknownColor(ColorgbErrors):
    def __init__(self, color:str):
        color = str(color).replace("'", "")
        super().__init__(f"Unknown Color. ({color})")
