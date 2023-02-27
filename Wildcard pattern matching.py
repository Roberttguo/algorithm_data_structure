'''
Given a text and a wildcard pattern, implement wildcard pattern matching algorithm that finds if wildcard pattern is
matched with text. The matching should cover the entire text (not partial text).
The wildcard pattern can include the characters '?' and '*'
'?' - matches any single character
'*' - Matches any sequence of characters (including the empty sequence)

For example,
Text = "baaabab",
Pattern = "*****ba*****ab", output : true
Pattern = "baaa?ab", output : true
Pattern = "ba*a?", output : true
Pattern = "a*ab", output : false
'''

def strmatching(s, pattern):
    m, n = len(pattern),len(s)
    print m, n
    """dp is a way to solve this efficiently."""
    """initialization of dp matrix"""
    dp = [[False]*(n + 1) for _ in range(m + 1)]#row to s, coloumn to pattern
    print dp
    dp[0][0] = True #when s and pattern are none, return True
    #when s is not empty, pattern is empty, matching is False
    #for i in range(1, m):#actually no need to reset to False anymore, alread initialized
    #    dp[i][0] = False

    #when s is empty, pattern is not empty, matching is False
    for j in range(1, m):
        dp[0][j] = dp[0][j-1] if pattern[j-1] == "*" else False

    """Fill remaining elements in dp"""
    for i in range(1, m):
        for j in range(1, n):
            if s[i-1] == pattern[j-1] or pattern[j-1] == '?': #pay attention, must check previous index
                dp[i][j] = dp[i-1][j-1]
            else:
                if pattern[j-1] == '*': #single char matching or empty matching
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                else:
                    dp[i][j] = False
    print m,n
    print dp
    return dp[m][n]



s="abcd"
p="a*d"
print "matching?", strmatching(s,p)
exit(0)
s="baaabab"
p="*****ba*****ab"
print "matching?", strmatching(s,p)