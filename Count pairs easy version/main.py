def solve(n, x, a):
    # initialize counter
    cnt = 0

    # iterate over all pairs of indices (i, j) such that i < j
    for i in range(n):
        for j in range(i + 1, n):
            # check if a[i] >= i, a[j] >= j, and a[i] + a[j] <= x
            if a[i] >= i and a[j] >= j and a[i] + a[j] <= x:
                # increment counter
                cnt += 1

    return cnt


# test the function
print(solve(4, 13, [9, 4, 7, 3]))
print(solve(4, 7, [4, 4, 1, 3]))
print(solve(10, 14, [5, 2, 1, 10, 3, 7, 8, 2, 15, 21]))
