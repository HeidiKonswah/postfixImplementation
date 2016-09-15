class Stack:
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return (self.items == [])

def evalPostfix(exp):
    import re
    tokenList = re.split("([^0-9])", exp)
    stack = Stack()
    for token in tokenList:
        if token == '' or token == ' ':
            continue
        if token == '+':
            SUM = stack.pop() + stack.pop()
            stack.push(SUM)
        elif token == '*':
            product = stack.pop() * stack.pop()
            stack.push(product)
        elif token == '-':
            result = stack.pop() - stack.pop()
            stack.push(result)
        elif token == '/':
            result1 = stack.pop() / stack.pop()
            stack.push(result1)
        else:
            stack.push(int(token))
    return stack.pop()

print evalPostfix("2 3 +")
        
