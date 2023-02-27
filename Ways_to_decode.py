'''
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.

'''



def ways(s):
    # print (s)
    if len(s) == 0:  # empty string can be decoded as 1 way
        return 1
    if len(s) == 1 and int(s) > 0:
        return 1
    if s[0] == '0':
        return 0
    count = 0
    if int(s[0]) > 0:
        count = ways(s[1:])
    if 10 <= int(s[0:2]) <= 26:
        count += ways(s[2:])
    return count


def ways_dp(s):
    m = len(s)
    dp = [0] * (m + 1)
    dp[0] = 1
    dp[1] = 1
    if s[0] == '0':
        return 0
    for i in range(2, m + 1):
        dp[i] = 0
        if s[i - 1] > '0':
            dp[i] = dp[i - 1]
        if s[i - 2] == '1' or s[i - 2] == '2' and s[i - 1] < '7':
            dp[i] += dp[i - 2]
    return dp[m]


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        def ways(s, mem):
            if s in mem:
                return mem[s]

            if s[0] == "0":
                return 0
            if len(s) == 1:
                return 1
            cnt = ways(s[1:], mem)
            if len(s) > 1 and (s[0:2] >= '10' and s[0:2] <= '26'):
                cnt += ways(s[2:], mem)
            mem[s] = cnt
            return cnt

        mem = {}
        mem[""] = 1
        return ways(s, mem)

o=Solution()
s = "111"

print("result=", ways(s))
print("result_=", ways_dp(s))
print(o.numDecodings(s))
s = "17"

print("result=", ways(s))
print("result_=", ways_dp(s))
print(o.numDecodings(s))
s = "17235"

print("result=", ways(s))
print("result_=", ways_dp(s))
print(o.numDecodings(s))
s = "1234"

print("result=", ways(s))
print("result_=", ways_dp(s))
print(o.numDecodings(s))