
class Token:

    useColors = True

    def __init__(self, type:str, value:str = ""):
        self.type = type
        self.value = value

    def __str__(self):
        color = "\033[1;36m" if Token.useColors else ""
        resetColor = "\033[0m" if Token.useColors else ""

        if self.value != "":
            return f"{color}{self.type}:{resetColor}{self.value}"
        return f"{color}{self.type}{resetColor}"

