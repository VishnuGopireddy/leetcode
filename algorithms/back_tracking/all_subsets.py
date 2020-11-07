class Subsets:
    def __init__(self):
        pass

    def subsets(self,s):
        n = len(s)
        subs = [None for i in range(n)]
        self.helper(s, subs, n)
        print(self.count)

    def helper(self,s,subs,k):
        if k == 0:
            print(subs)
            # self.print_subsets(subs)
            # print(self.check_palin(subs))
            return
        else:
            subs[k-1] = None
            self.helper(s,subs,k-1)
            subs[k-1] = s[k-1]
            self.helper(s, subs, k - 1)

if __name__=='__main__':
    subs = Subsets()
    subs.subsets('aaaa')