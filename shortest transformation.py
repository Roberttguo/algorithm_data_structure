'''

'''

import heapq


def BFS(s, e, words):
    Q = [(0, s)]
    while len(Q) > 0:
        tmp = heapq.heappop(Q)
        if tmp[1] == e:
            return tmp[0]
        for i in range(26):
            for j in range(len(tmp[1])):
                tmp2 = chr(ord('a') + i)
                if tmp2!=tmp[1][j]:
                    newtmp = tmp[1][0:j] + tmp2 + tmp[1][j + 1:]
                    if newtmp in words:
                        print ("new tmp: ", newtmp)
                        heapq.heappush(Q, (tmp[0] + 1, newtmp))
                        words.remove(newtmp)  # assume this is right python method

    return 0

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log", "cog"]
print (BFS(beginWord, endWord, wordList))

wordList =["hot","dot","dog","lot","log"]
beginWord = "hit"
endWord = "cog"

print (BFS(beginWord, endWord, wordList))

wordList =["hot","dot","dog","lot","log","cog"]
beginWord = "hit"
endWord = "hot"

print (BFS(beginWord, endWord, wordList))