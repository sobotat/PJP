import sys
from Scanner import Scanner

def execute(data:str, useColors:bool):
    data = data.strip()
    print(f"\033[1;34mInput:\033[0m\n{data}")

    color = "\033[1;36m" if useColors else ""
    resetColor = "\033[0m" if useColors else ""

    print(f"\n\033[1;34mOut:\033[0m")
    for token in Scanner().process(data):
        if token.value != "":
            print(f"{color}{token.type}:{resetColor}{token.value}")
            continue
        print(f"{color}{token.type}{resetColor}")

def main():
    filename = ""
    useColors = True

    for i in range(len(sys.argv)):
        if sys.argv[i] == "-nc":
            useColors = False
        elif sys.argv[i] == "-f":
            filename = sys.argv[i + 1]
            i += 1

    data = ""
    if filename == "":
        try:
            while True:
                data += input() + "\n"
        except EOFError:
            pass
    else:
        try:
            with open(filename, "r") as f:
                data = f.read()
                f.close()
        except FileNotFoundError:
            print("Error: File not found!")
            return

    execute(data, useColors)

if __name__ == '__main__':
    main()