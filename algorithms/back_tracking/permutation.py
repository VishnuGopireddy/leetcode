class Permute:
    '''
    A permutation is a rearrangement of members of a sequence into a new sequence.
    For example, there are 24 permutations of [a, b, c, d].
    Some of them are [b, a, d, c], [d, a, b, c] and [a, d, b, c].
    '''
    def __init__(self):
        self.count = 0

    def permute(self, arr, l, r):
        if l == r:
            self.count = self.count + 1
            print(self.count, arr)
        #             if self.count == 3:
        #                 print(arr,self.count)
        else:
            for i in range(l, r + 1):
                #                 print(l,r,i)
                arr[i], arr[l] = arr[l], arr[i]
                self.permute(arr, l + 1, r)
                arr[i], arr[l] = arr[l], arr[i]


per = Permute()
per.permute([1, 2, 3], 0, 2)