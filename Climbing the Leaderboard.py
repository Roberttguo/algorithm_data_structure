'''
An arcade game player wants to climb to the top of the leaderboard and track their ranking. The game uses Dense Ranking, so its leaderboard works like this:

The player with the highest score is ranked number  on the leaderboard.
Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.
Example



The ranked players will have ranks , , , and , respectively. If the player's scores are ,  and , their rankings after each game are ,  and . Return .

Function Description

Complete the climbingLeaderboard function in the editor below.

climbingLeaderboard has the following parameter(s):

int ranked[n]: the leaderboard scores
int player[m]: the player's scores
Returns

int[m]: the player's rank after each new score
Input Format

The first line contains an integer , the number of players on the leaderboard.
The next line contains  space-separated integers , the leaderboard scores in decreasing order.
The next line contains an integer, , the number games the player plays.
The last line contains  space-separated integers , the game scores.
'''

#accepted on 8/4/2021 at hackerrank.com=>medium
def findIndex(arr, e):
    #arr is sorted in desending order
    l,r=0,len(arr)-1
    while l<=r:
        mid=(l+r)/2
        print "mid=?", mid, arr[mid]
        if arr[mid]==e:
            return mid
        if arr[mid]>e:
            if mid==len(arr)-1:
                return len(arr)
            if mid<len(arr)-1 and arr[mid+1]<=e:
                return mid+1
            l=mid+1
            continue
        if arr[mid]<e:
            if mid==0:
                return 0
            if mid >0 and arr[mid-1]>e:
                return mid
            r=mid-1
            continue

def climbingLeaderboard(ranked, player):
    # Write your code here
    rank=[1]
    for i in range(1,len(ranked)):
        if ranked[i]==ranked[i-1]:
            rank.append(rank[-1])
        else:
            rank.append(rank[-1]+1)
    print rank
    res=[]
    for score in player:
        ind= findIndex(ranked, score)
        print 'ind= ', ind
        if ind==len(ranked):
            res.append(rank[-1]+1)
        else:
            res.append(rank[ind])
    return res

ranked=[100, 100, 50, 40, 40, 20, 10]
player=[5,25,50,120]

print climbingLeaderboard(ranked, player)