class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def size(self):
        return len(self.items)


def check_brackets(sequence):
    stack = Stack()
    brackets = {'(': ')', '[': ']', '{': '}'}

    for char in sequence:
        if char in brackets:
            stack.push(char)
        elif char in brackets.values():
            if stack.is_empty():
                return "Несбалансированно"
            top = stack.pop()
            if brackets[top] != char:
                return "Несбалансированно"

    return "Сбалансированно" if stack.is_empty() else "Несбалансированно"


# Примеры использования
examples = [
    "(((([{}]))))",
    "[([])((([[[]]])))]{()}",
    "{{[()]}}",
    "}{",
    "{{[(])]}}",
    "[[{())}]"
]

for ex in examples:
    print(f"{ex}: {check_brackets(ex)}")