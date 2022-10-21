def solve(n, arr):

    max_pir = max(arr)

    for i in xrange(0, n):

        if arr[i] != max_pir:
            continue

        if i > 0 and arr[i-1] != max_pir:
            return i+1
        elif i < n-1 and arr[i+1] != max_pir:
            return i+1

    return -1


if __name__ == "__main__":

    t = int(raw_input())

    for _ in xrange(0, t):
        n = int(raw_input())
        arr = map(int, raw_input().split(" "))
        print solve(n, arr)
