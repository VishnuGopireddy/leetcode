class Solution:
    def eval(self,num1,op,num2):
        if op == '+':
            return num1 + num2
        if op == '-':
            return num1 - num2
        if op == '*':
            return num1 * num2
        if op == '/':
            return num1 // num2

    def calculate(self, s):
        stack = []
        i = 0
        total = 0
        n = len(s)

        while i < n:
            num = ''
            if s[i].isdigit():
                while i<n and s[i].isdigit():
                    num += s[i]
                    i += 1
                i -= 1
                num = int(num)
                if len(stack) > 0:
                    if stack[-1] == '*' or stack[-1] == '/':
                        op = stack.pop(-1)
                        num1 = stack.pop(-1)
                        num = self.eval(num1,op,num)
                stack.append(num)

            elif s[i] == '+' or s[i] == '-':
                stack.append(s[i])

            elif s[i] == '*' or s[i] == '/':
                stack.append(s[i])

            print(stack)
            i += 1

        total = stack.pop(0)
        while len(stack) > 0:
            op = stack.pop(0)
            total = self.eval(total,op,stack.pop(0))

        return (total)

if __name__=='__main__':
    s = '1 + 2 * 3 +14/2'
    sol = Solution()
    print(sol.calculate(s))
