def longestPalindrome(s, m):
    # preprocess the string by adding special characters to it
    t = "^#" + "#".join(s) + "#$"
    n = len(t)
    p = [0] * n
    c = r = 0
    for i in range(1, n - 1):
        # check if the current position is within the rightmost palindrome
        if i < r:
            # get the mirrored position of i with respect to c
            mi = 2 * c - i
            # get the palindrome length at the mirrored position
            p[i] = min(r - i, p[mi])
        # expand the palindrome at the current position
        while t[i + p[i] + 1] == t[i - p[i] - 1]:
            p[i] += 1
        # update the center and rightmost position of the palindrome
        if i + p[i] > r:
            c, r = i, i + p[i]
    # find the maximum palindrome length
    maxLen = 0
    for i in range(1, n - 1):
        # check if the palindrome at the current position is valid
        isValid = True
        for j in range(p[i]):
            if t[i - j - 1] != t[i + j + 1]:
                isValid = False
                break
        if isValid:
            maxLen = max(maxLen, p[i])
    return maxLen


s = "bccbaabcx"
m = ["a", "b", "c", "v"]
print(longestPalindrome(s, m))  # prints 6

s = "abba"
m = ["a", "b"]
print(longestPalindrome(s, m))  # prints 4
