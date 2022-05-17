class RPNStack:
    """
    This class represents a stack to which operands are added.
    It implements usual stack methods and a method to evaluate a RPN expression.
    """

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
        """
        Operands are added to a stack and when an operator is found, the last 2 operands are popped
        from the stack and the result is pushed back onto the stack.

        :param expression: string given as input from the user, that represents a RPN expression
        :return: the evaluation of the expression given or 0 if the expression is misspelled
        """
        tokenList = expression.split(" ")

        for token in tokenList:

            if token in RPNStack.operators:
                op2 = self.pop()
                op1 = self.pop()
                result = RPNStack.operators[token](op1, op2)
                self.push(result)
            else:
                try:
                    token = int(token)
                except ValueError as e:
                    self.somethingWrong = True
                    return 0
                self.push(token)
        return self.pop()



if __name__ == '__main__':
    print('This program calculates PRM expressions')
    print('Write your expression in PRN format or write q to close the calculator')

    try:
        while True:
            stack = RPNStack()
            expression = input(">")
            if expression == 'q':
                exit(0)
            result = stack.evaluateExpression(expression=expression)
            if stack.somethingWrong:
                print("You mistyped your expression, try again!")
            elif not stack.isEmpty():
                print("This is not a valid expression! Enter a valid one.")
            else:
                print(result)

    except (KeyboardInterrupt, EOFError):
        pass




