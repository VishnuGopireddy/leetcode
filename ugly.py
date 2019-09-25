def ugly(num):
    ugly = 0
    while num > 1 and ugly == 0:
        if num % 2 == 0:
            num = num // 2
        elif num % 3 == 0:
            num = num // 3
        elif num % 5 == 0:
            num = num // 5
        else:
            ugly = 1
    return ugly

num = 6
print(ugly(num))