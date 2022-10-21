def solve(s):

    max_diff = 0
    prev_idx = -1

    s = s + 'D' # destination
    s = 'S' + s  # source

    n = len(s)

    for i in xrange(0, n):

        if s[i] == 'S':
            prev_idx = i
        elif s[i] == 'R':
            max_diff = max(max_diff, i - prev_idx)
            prev_idx = i
        elif s[i] == 'D':
            max_diff = max(max_diff, i - prev_idx)

    return max_diff


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        s = raw_input()
        results.append(solve(s))

    for result in results:
        print result
