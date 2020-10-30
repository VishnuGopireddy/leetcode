class Solution:
    def calculate(self, s):
        total = 0
        sign = 1
        n = len(s)
        queue = []
        num = 0
        i = 0
        print(n)
        while i < n:
            # number
            if s[i].isdigit():
                num = ''
                while i < n and s[i].isdigit():
                    num += s[i]
                    i += 1
                    print(num,i)
                if len(num) > 0:
                    num = int(num)
                total += (num * sign)
                i -= 1
            # sign
            elif s[i] == '+':
                sign = 1
            elif s[i] == '-':
                sign = -1
            # (
            elif s[i] == '(':
                queue.append(total)
                queue.append(sign)
                total = 0
                sign = 1
            # )
            if s[i] == ')':
                sign = queue.pop(-1)
                num = queue.pop(-1)
                print(sign)
                print(num)
                total = total * sign
                total += num
                # queue.append(total)


            print(s[i])
            print(queue)
            print(total)
            print('-------------')
            i += 1

        return total


if __name__ == '__main__':
    s = '2+(1+(4+5+2)-3)+(6-8)'
    s = '101'
    s = '1-(5)'
    # s = '1-5+2-10'
    sol = Solution()
    print(sol.calculate(s))