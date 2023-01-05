def solve(x):
    y = int(str(x)[::-1])  # reverse x
    xy = fast_exp(x, y, 1000000007)  # xy modulo 109+7
    yx = fast_exp(y, x, 1000000007)  # yx modulo 109+7
    if xy > yx:
        return "Alice"
    elif yx > xy:
        return "Bob"
    else:
        return "Draw"


# fast exponentiation function
def fast_exp(x, y, mod):
    result = 1
    while y > 0:
        if y % 2 == 1:
            result = (result * x) % mod
        x = (x * x) % mod
        y = y // 2
    return result


# test the function
print(solve(13))  # should print "Bob"
print(solve(125))  # should print "Alice"
print(solve(4))  # should print "Draw"
