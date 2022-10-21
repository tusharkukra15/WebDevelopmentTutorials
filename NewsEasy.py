def solve(s):

    target = "heidi"
    j = 0
    t_len = len(target)
    s_len = len(s)
    for i in xrange(0, s_len):
        if s[i] == target[j]:
            j += 1
            if j == t_len:
                break

    return "YES" if j == t_len else "NO"


if __name__ == "__main__":

    s = raw_input()
    print solve(s)
