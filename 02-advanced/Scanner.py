from Token import Token

def split(text:str, token: list) -> list[str]:
    out = []
    current = ""
    for c in text.strip().replace('\r', ''):
        if c == "\n" or c == " ":
            if current != "":
                out.append(current)
                current = ""
            if c == "\n":
                out.append("\n")
            continue
        elif "0" < c > "9" and current.isnumeric():
            out.append(current)
            current = ""

        current += c

        for t in token:
            if t not in current:
                continue
            if t != current and current.split(t)[0] != "":
                out.append(current.split(t)[0])
            out.append(t)
            current = ""

    if len(current) != 0:
        out.append(current)
    return out

class Scanner:

    def __init__(self, data):
        self.data = data

    def process(self) -> list[Token]:
        tokens = split(self.data, ["(", ")", "+", "-", "*", ";"])
        print(f"\n{tokens}")

        isComment = False
        for token in tokens:
            if token == "//" or isComment:
                isComment = False if token == "\n" else True
                continue

            if token in ["+", "-", "*"]:
                yield Token("OP", token)
            elif token == "div":
                yield Token("DIV")
            elif token == "(":
                yield Token("LPAD")
            elif token == ")":
                yield Token("RPAD")
            elif token == ";":
                yield Token("SEMICOLON")
            elif token.isnumeric():
                yield Token("NUM", token)
            elif token == "mod":
                yield Token("MOD")
            elif token != "\n":
                yield Token("ID", token)