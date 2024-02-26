from Token import Token

class Scanner:

    @staticmethod
    def process(data:str) -> list[Token]:
        isComment = False
        for token in Scanner.split(data,["(", ")", "+", "-", "*", ";"]):
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

    @staticmethod
    def split(text: str, token: list) -> list[str]:
        current = ""
        for c in text.strip().replace('\r', ''):
            if c == "\n" or c == " ":
                if current != "":
                    yield current
                    current = ""
                if c == "\n":
                    yield "\n"
                continue
            elif "0" < c > "9" and current.isnumeric():
                yield current
                current = ""

            current += c

            for t in token:
                if t not in current:
                    continue
                if t != current and current.split(t)[0] != "":
                    yield current.split(t)[0]
                yield t
                current = ""

        if len(current) != 0:
            yield current