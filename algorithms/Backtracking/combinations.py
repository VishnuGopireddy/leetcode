'''
cat :cat
     cta
     act
     atc
     tac
     tca

No of combinations are n!
'''

class Comb:
    def __init__(self):
        self.sol = []

    def combinations(self,s):
        l = 0
        r = len(s) - 1
        s_l = [i for i in s]
        self.helper_comb(s_l, l, r)

        sol = [(i.split()) for i in set(comb.sol)]
        return ([[int(j) for j in i] for i in sol])


    def helper_comb(self,s, l, r):
        if l == r:
            a = s.copy()
            self.sol.append(' '.join(a))
            print(a)
            return a
        else:
            for i in range(l, r+1):
                s[l], s[i] = s[i], s[l]
                self.helper_comb(s, l+1, r)
                s[l], s[i] = s[i],s[l]

if __name__ == '__main__':
    comb = Comb()
    print(comb.combinations('112'))
