def solve(a, b):

    len_a = len(a)
    len_b = len(b)

    bits_xored_subarr_a = 0
    bits_xored_b = 0

    # b and first sub-array of a
    for i in xrange(0, len_b):
        if a[i] == '1':
            bits_xored_subarr_a ^= 1
        if b[i] == '1':
            bits_xored_b ^= 1

    count = 0

    # inner sub-arrays of a
    for i in xrange(len_b, len_a):
        if bits_xored_subarr_a == bits_xored_b:
            count += 1
        if a[i] == '1':
            bits_xored_subarr_a ^= 1
        if a[i - len_b] == '1':
            bits_xored_subarr_a ^= 1

    # for the last sub-array of a
    if bits_xored_subarr_a == bits_xored_b:
        count += 1

    return count
