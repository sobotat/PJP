
def split(text:str, token:list) -> list[str]:
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
            if t in current and t != current and current.split(t)[0] != "":
                out.append(current.split(t)[0])
            out.append(t)
            current = ""

    if len(current) != 0:
        out.append(current)
    return out

def process(data:str, useColors=True) -> str:
    out = ""
    tokens = split(data, ["(", ")", "+", "-", "*", ";"])
    #print(f"\n{tokens}")

    color = "\033[1;36m" if useColors else ""
    resetColor = "\033[0m" if useColors else ""

    isComment = False
    for token in tokens:
        if token == "//" or isComment:
            isComment = False if token == "\n" else True
            continue

        if token in ["+", "-", "*"]:
            out += f"{color}OP:{resetColor}{token}\n"
        elif token == "div":
            out += f"{color}DIV{resetColor}\n"
        elif token == "(":
            out += f"{color}LPAD{resetColor}\n"
        elif token == ")":
            out += f"{color}RPAD{resetColor}\n"
        elif token == ";":
            out += f"{color}SEMICOLON{resetColor}\n"
        elif token.isnumeric():
            out += f"{color}NUM:{resetColor}{token}\n"
        elif token == "mod":
            out += f"{color}MOD{resetColor}\n"
        else:
            out += f"{color}ID:{resetColor}{token}\n"

    return out.strip()


def main():
    data = ""
    try:
        while True:
            data += input() + "\n"
    except EOFError:
        data = data.strip()
        print(f"\033[1;34mInput:\033[0m\n{data}")
        print(f"\n\033[1;34mOut:\033[0m\n{process(data)}")

if __name__ == '__main__':
    main()