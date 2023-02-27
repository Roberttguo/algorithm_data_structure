'''
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than 104 for all the given inputs.



Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 4, denominator = 333
Output: "0.(012)"

'''

#Accepted 2/28/2022
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        sign = False
        if numerator < 0 and denominator > 0 or numerator > 0 and denominator < 0:
            sign = True

        numerator = abs(numerator)
        denominator = abs(denominator)

        q = numerator / denominator
        r = numerator % denominator
        if r == 0:
            return str(q) if not sign else "-" + str(q)

        ans = []
        ans.append(str(q))
        ans.append(".")
        rem_map = {}
        while r != 0:
            if r in rem_map:
                ans.insert(rem_map[r], "(")
                ans.append(")")
                break
            else:
                rem_map[r] = len(ans)
                r *= 10
                q = r / denominator
                r %= denominator
                ans.append(str(q))
        return "".join(ans) if not sign else "-" + "".join(ans)