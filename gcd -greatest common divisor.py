def nthUglyNumber(n, a, b, c):
    """
    :type n: int
    :type a: int
    :type b: int
    :type c: int
    :rtype: int
    """
    arr = [1]
    idx_a, idx_b, idx_c = 0, 0, 0
    while len(arr) < n + 1:
        va = a * arr[idx_a]
        vb = b * arr[idx_b]
        vc = c * arr[idx_c]
        min_v = min(va, vb, vc)
        if min_v == va:
            idx_a += 1
        if min_v == vb:
            idx_b += 1
        if min_v == vc:
            idx_c += 1
        arr.append(min_v)
    print ('arr=', arr)
    return arr[n]

nthUglyNumber(5,2,11,13)




def gcd(a,b):
    if min(a,b)==0:
        return max(a,b)
    if max(a,b)%min(a,b)==0:
        return min(a,b)
    return gcd(max(a,b)%min(a,b), min(a,b))


print ("gcd=", gcd(8,54))

print ("gcd=", gcd(0,121))

print ("gcd=", gcd(12,121))

print ("gcd=", gcd(11,121))