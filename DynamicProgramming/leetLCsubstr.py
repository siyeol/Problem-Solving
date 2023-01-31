user0 = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
user1 = ["/start", "/pink", "/register", "/orange", "/red", "a"]

def findLH(u1, u2):
    n = len(u1)
    m = len(u2)

    dp = [[0]*(n+1) for _ in range(m+1)]

    length = 0
    yy, xx = 0, 0
    for x in range(1, n+1):
        for y in range(1, m+1):
            if u1[x-1] == u2[y-1]:
                dp[y][x] = dp[y-1][x-1]+1
                if length < dp[y][x]:
                    length = dp[y][x]
                    yy = y
                    xx = x
            else:
                dp[y][x] = 0

    result = [""] * length
    while dp[yy][xx] != 0:
        length-=1
        result[length] = u1[xx-1]

        xx-=1
        yy-=1

    return result

print(findLH(user0, user1))