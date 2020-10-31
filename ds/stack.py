class Stack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> None:
        return self.stack.pop(-1)

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def get_len(self):
        return len(self.stack)

    def print_stack(self):
        print(self.stack)

if __name__ == '__main__':
    stack = Stack()
    eles = [10,20,30,40,50]
    for ele in eles:
        stack.push(ele)
    print('Poped', stack.pop())
    print(stack.top())
    stack.print_stack()