def num_pairs(n, x, a):
    a.sort()  # sort the array in non-decreasing order

    num_pairs = 0
    for i in range(n):
        j = binary_search(a, i, i, n - 1, x - a[i])  # find largest j such that a[j] >= j and a[i] + a[j] <= x
        num_pairs += j - i  # add the number of valid pairs (i, j) to the total

    return num_pairs


def binary_search(a, i, l, r, x):
    # find largest j such that a[j] >= j and a[i] + a[j] <= x
    while l < r:
        mid = (l + r + 1) // 2
        if a[mid] < mid or a[mid] + a[i] > x:
            r = mid - 1
        else:
            l = mid
    return l


n = 4
x = 13
a = [9, 4, 7, 3]
print(num_pairs(n, x, a))
