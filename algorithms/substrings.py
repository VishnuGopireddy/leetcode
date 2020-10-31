class Substrings:
    def __init__(self):
        pass

    def substring(self,s):
        self.helper(s,[0,0,0],len(s))

    def helper(self,s,sub,k):
        if k == 0:
            print(s)
        else:
            for i in range(k):
                sub[i] = s[i]
                self.helper(s,sub,k-1)



if __name__=='__main__':
    s = 'abc'
    substr = Substrings()
    substr.substring(s)