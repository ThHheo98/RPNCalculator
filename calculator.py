class PRNStack:
    operators = {
        "+": (lambda a, b: a + b),
        "-": (lambda a, b: a - b),
        "*": (lambda a, b: a * b),
        "/": (lambda a, b: int(a / b)),
        "%": (lambda a, b: a % b)
    }

    def __init__(self):
        self.items = []
        self.somethingWrong = False

    def isEmpty(self):
        return self.items == []

    def push(self, items):
        self.items.append(items)

    def pop(self):
        return self.items.pop()

    def evaluateExpression(self, expression):
        tokenList = expression.split(" ")

        for token in tokenList:
            # Check is the token is an operator or an operand!
            if token in PRNStack.operators:
                op2 = self.pop()
                op1 = self.pop()
                result = PRNStack.operators[token](op1, op2)
                self.push(result)
            else:  # Toke is an Operand
                try:
                    token = int(token)
                except ValueError as e:
                    self.somethingWrong = True
                    return 0
                self.push(token)

        print(self.items)
        return self.pop()



if __name__ == '__main__':
    print('This program calculates PRM expressions')
    print('Write your expression in PRN format or write q to close the calculator')

    try:
        while True:
            stack = PRNStack()
            expression = input(">")
            if expression == 'q':
                exit(0)
            result = stack.evaluateExpression(expression=expression)
            print(stack.items)
            if stack.somethingWrong:
                print("You mistyped your expression, try again!")
            elif not stack.isEmpty():
                print("This is not a valid expression! Enter a valid one.")
            else:
                print(result)

    except (KeyboardInterrupt, EOFError):
        pass




