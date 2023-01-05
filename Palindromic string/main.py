def solve(n, s, m, valid_chars):
    # initialize set of valid characters
    valid = set()
    for c in valid_chars:
        valid.add(c)

    # initialize maximum length palindrome substring
    max_len = -1

    # iterate over all substrings of s
    for i in range(n):
        for j in range(i + 1, n + 1):
            # check if substring is a palindrome and consists only of valid characters
            if s[i:j] == s[i:j][::-1] and all(c in valid for c in s[i:j]):
                # update maximum length palindrome substring
                max_len = max(max_len, j - i)

    return max_len


# test the function
print(solve(9, "bccbaabcx", 4, "abcv"))  # should print 6
print(solve(4, "abba", 2, "ab"))  # should print 4
print(solve(6, "abaacb", 1, "z"))  # should print -1
