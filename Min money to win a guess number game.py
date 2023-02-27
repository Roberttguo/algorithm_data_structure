'''
We are playing the Guessing Game. The game will work as follows:

I pick a number between 1 and n.
You guess a number.
If you guess the right number, you win the game.
If you guess the wrong number, then I will tell you whether the number I picked is higher or lower, and you will continue guessing.
Every time you guess a wrong number x, you will pay x dollars. If you run out of money, you lose the game.
Given a particular n, return the minimum amount of money you need to guarantee a win regardless of what number I pick.



Example 1:
Input: n = 10
Output: 16
Explanation: The winning strategy is as follows:
- The range is [1,10]. Guess 7.
    - If this is my number, your total is $0. Otherwise, you pay $7.
    - If my number is higher, the range is [8,10]. Guess 9.
        - If this is my number, your total is $7. Otherwise, you pay $9.
        - If my number is higher, it must be 10. Guess 10. Your total is $7 + $9 = $16.
        - If my number is lower, it must be 8. Guess 8. Your total is $7 + $9 = $16.
    - If my number is lower, the range is [1,6]. Guess 3.
        - If this is my number, your total is $7. Otherwise, you pay $3.
        - If my number is higher, the range is [4,6]. Guess 5.
            - If this is my number, your total is $7 + $3 = $10. Otherwise, you pay $5.
            - If my number is higher, it must be 6. Guess 6. Your total is $7 + $3 + $5 = $15.
            - If my number is lower, it must be 4. Guess 4. Your total is $7 + $3 + $5 = $15.
        - If my number is lower, the range is [1,2]. Guess 1.
            - If this is my number, your total is $7 + $3 = $10. Otherwise, you pay $1.
            - If my number is higher, it must be 2. Guess 2. Your total is $7 + $3 + $1 = $11.
The worst case in all these scenarios is that you pay $16. Hence, you only need $16 to guarantee a win.
Example 2:

Input: n = 1
Output: 0
Explanation: There is only one possible number, so you can guess 1 and not have to pay anything.
Example 3:

Input: n = 2
Output: 1
Explanation: There are two possible numbers, 1 and 2.
- Guess 1.
    - If this is my number, your total is $0. Otherwise, you pay $1.
    - If my number is higher, it must be 2. Guess 2. Your total is $1.
The worst case is that you pay $1.

'''

import sys
import time
class Solution:
    """
            Consider the numbers are in range 1-n.
            We need to check for all numbers from 1 to n for which the total penalty is minimum.
            Suppose we guessed a number k between 1-n, therefore, our penalty would be =>
                k + max(penalty for numbers in the range 1 to k-1, penalty for numbers in the range k+1 to n)
                as after every guess we would know when the target is lower than or greater than our guess.
            Now we just need to find the penalty for all k in the range 1-n and the k which gives the minimum penalty would be our answer.
        """


    def dp(self, start, end, lookup):
        if start >= end:
            return 0
        if (start, end) not in lookup:
            money = sys.maxsize
            for penalty in range(start, end+1):
                money = min(money, penalty + max(self.dp(start, penalty - 1, lookup), self.dp(penalty+1, end, lookup)))
            lookup[(start, end)] = money
        return lookup[(start, end)]

    def getMoneyAmount(self, n):
        return self.dp(1, n, {})

o=Solution()
print o.getMoneyAmount(10)
#print o.getMoneyAmount2(10)
print o.getMoneyAmount(16)
#print o.getMoneyAmount2(16)

print o.getMoneyAmount(5)
#print o.getMoneyAmount2(5)
print o.getMoneyAmount(1)
print o.getMoneyAmount(2)
#print o.getMoneyAmount2(2)

s=time.time()
print o.getMoneyAmount(30)
e=time.time()
d1=e-s

