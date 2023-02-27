'''


'''


def myAtoi(s):
    """
    :type s: str
    :rtype: int
    """
    sign = False

    ans = ""
    for x in s:
        print("x is:", x, x=='-')
        if x == "-":
            sign = True
            continue

        if x.isspace() or x == "+" or not x.isdigit():
            continue
        if x.isdigit():
            if x == '0':
                if len(ans) > 0:
                    ans += x
                else:
                    continue
            else:
                ans += x
    print ("sign is:", sign)
    res = int(ans)
    if sign:
        return -res if -res > -2 ** 31 else -2 ** 31
    else:
        return res if res <= 2 ** 31 - 1 else 2 ** 31 - 1

s="   -42"

print ("res=",myAtoi(s))