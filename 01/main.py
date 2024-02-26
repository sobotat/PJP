
def split(text:str, token:list) -> list[str]:
    tokens = []
    current = ""
    for c in text.replace(' ', '').replace('\n', '').replace('\r', ''):
        if c in token:
            if len(current) != 0:
                tokens.append(current)
                current = ""
            tokens.append(c)
        else:
            current += c

    if len(current) != 0:
        tokens.append(current)
    return tokens

    
def applyOperator(operator, operand1, operand2) -> float:
    match operator:
        case '+':
            return operand1 + operand2
        case '-':
            return operand1 - operand2
        case '*':
            return operand1 * operand2
        case '/':
            if operand2 != 0:
                return operand1 / operand2
            else:
                raise ZeroDivisionError
    raise ValueError("Invalid operator")
    
def calculate(expression:str) -> str:
    tokens = split(expression, ['*', '/', '+', '-', '(', ')'])
    priorities = ['*', '/', '+', '-']
    numbers = []
    operators = []
    
    try:
        token:str
        for token in tokens:
            if token.isnumeric():
                numbers.append(int(token))
            elif token in {'+', '-', '*', '/', '('}:
                operators.append(token)
            elif token == ')':
                while operators[len(operators) - 1] != '(':
                    first = numbers.pop()
                    last = numbers.pop()
                    numbers.append(applyOperator(operators.pop(), last, first))
                operators.pop()
            else:
                return "ERROR"   

        while len(operators) != 0:
            for priority in priorities:
                if priority in operators:
                    index = operators.index(priority)
                    operators.pop(index)
                    
                    numbers[index] = applyOperator(priority, numbers[index], numbers[index + 1])
                    numbers.pop(index + 1)                    

                    if len(operators) == 0:
                        return str(numbers[index])
                    
                    break
        return str(numbers[0])
    except ZeroDivisionError:
        return "Error"
    except Exception as e:
        #print(e)
        return "Error"

def main():
    n = int(input())
    for _ in range(n):
        expression = input()
        result = calculate(expression)
        print(f"{result}")

if __name__ == "__main__":
    main()