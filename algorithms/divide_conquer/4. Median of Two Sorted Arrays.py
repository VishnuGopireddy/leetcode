#https://youtu.be/LPFhl65R7ww
class MergeSorted:
    def __init__(self):
        pass

    def partition(self,nums1, nums2):
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 < n2:
            x = nums1
            y = nums2
        else:
            x, y = nums2, nums1
        nums1 = x; nums2 = y
        if len(x) == 0:
            n2 = len(y)
            if n2 % 2:
                return y[n2 // 2]
            else:
                return (y[(n2//2)-1] + y[n2//2]) / 2
        # x_par can take n1 + 1

        found = 0
        low = 0
        high = n1
        x_par = 0
        y_par = 0

        while low < high and found == 0:
            x_par = ((low + high) // 2)
            y_par = ((n1 + n2 + 1) // 2) - x_par
            print('--------',x_par, y_par)
            # maxleftX <= minRightY
            # maxleftY <= minRightX
            print('Left:', nums1[:x_par], nums2[:y_par])
            print('Right:', nums1[x_par:], nums2[y_par:])

            # print(nums1[x_par-1], nums2[y_par])
            # print(nums2[y_par-1], nums1[x_par])

            if x_par == 0:
                if nums2[y_par - 1] <= nums1[x_par]:
                    found = 1
                elif nums2[y_par-1] > nums1[x_par]:
                    x_par += 1
                continue

            if y_par == 1:
                if nums1[x_par-1] <= nums2[y_par-1]:
                    found = 1
                continue

            elif nums1[x_par-1] <= nums2[y_par] and nums2[y_par-1] <= nums1[x_par]:
                found = 1

            elif nums1[x_par-1] > nums2[y_par]:
                low = 0; high = x_par
                #move X_par to left
            elif nums2[y_par-1] > nums1[x_par]:
                #move X_par to right
                # x_par += 1
                low = x_par; high = high

        if (n1 + n2) % 2:
            return y[y_par]
        else:
            print(y[y_par], x[x_par])
            return (y[y_par]+x[x_par])/2

if __name__ == '__main__':
    nums1 = [1,2]
    nums2 = [3,4]
    ms = MergeSorted()
    print(ms.partition(nums1, nums2))