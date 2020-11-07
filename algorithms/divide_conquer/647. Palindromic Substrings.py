def pallandrim_substr(s):
    n = len(s)
    mat = [[0 for i in range(n+1)] for j in range(n+1)]
    mat[0][0] = 1
    for i in range(1,n+1):
        for j in range(1,n+1):
            if s[i-1] == s[j-1]:
                if s[i-2]  == s[j-2] and s[i-1] == s[i-2]:
                    # if mat[i-1][j-1] == 0:
                    #     mat[i-1][j-1] = 1
                    mat[i][j] = (mat[i-1][j-1] * 2)
                else:
                    mat[i][j] = max(mat[i-1][j],mat[i][j-1]) + 1
            else:
                mat[i][j] = max(mat[i - 1][j], mat[i][j - 1])

    print(mat)

pallandrim_substr('aaa')