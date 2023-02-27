'''
This problem was asked by Google.

You are given an N by N matrix of random letters and a dictionary of words. Find the maximum number of words
 that can be packed on the board from the given dictionary.

A word is considered to be able to be packed on the board if:

It can be found in the dictionary
It can be constructed from untaken letters by other words found so far on the board
The letters are adjacent to each other (vertically and horizontally, not diagonally).
Each tile can be visited only once by any word.

For example, given the following dictionary:

{ 'eat', 'rain', 'in', 'rat' }
and matrix:

[['e', 'a', 'n'],
 ['t', 't', 'i'],
 ['a', 'r', 'a']]

 Your function should return 3, since we can make the words 'eat', 'in', and 'rat' without them touching each other.
 We could have alternatively made 'eat' and 'rain', but that would be incorrect since that's only 2 words.
'''
class TrieNode():

    def __init__(self, char):
        self.isLeaf = False
        self.char = char
        self.children = {}

class Trie():
    def __init__(self):
        self.root = TrieNode("")
        self.ouput=[]# used to store all words containing a searching prefix

    def insert(self, word):
        node = self.root
        for ch in word: #ch single char
            if not ch in node.children:
                node.children[ch]=TrieNode(ch)
                node=node.children[ch]
            else:
                node =node.children[ch]
        #after a word is inserted, set current node's isLeaf=True
        node.isLeaf = True

    def find(self, word): # check if a word (maybe a prefix of another word) is in Trie
        node = self.root

        for ch in word:
            if not ch in node.children:
                return False
            node = node.children[ch]
        return True

    def find_word(self, word): # check if a word is in Trie
        node = self.root

        for ch in word:
            if not ch in node.children:
                return False
            node = node.children[ch]
        return node.isLeaf


    def search_all_prefix(self, word):
        node = self.root
        #first navigate to last node of word
        for ch in word:
            if ch in node.children:
                node = node.children[ch]
            else:
                #not found entire word, return []
                return []
        self.ouput =[]
        self.dfs(node, word[:-1])#word[:-1] = word[0:len(word)-1]

        return self.ouput

    def dfs(self, node, pre):
        if node.isLeaf:
            self.ouput.append(pre+node.char)

        for child_node in node.children.values():
            self.dfs(child_node, pre+node.char)

def maxPackedWords(arr, dictionary):
    shift =[[0,-1],[1,0],[0,1],[-1,0]]
    visited=[[False]*len(arr[0]) for _ in range(len(arr))]
    max_num=0
    def helper(arr, x,y, word, visited, words, dic):
        #tmp=""
        if not visited[x][y]:
            word+=arr[x][y]
            #tmp=arr[x][y]
            visited[x][y]=True
            #arr[x][y]="*"
        if word in dic:
            words.add(word)
        if x==len(arr)-1 and y==len(arr[0])-1:
            print ("number of found words: ", len(words), "found: ", words)
            return
        for dx, dy in shift:
            if 0<=x+dx<len(arr) and 0<=y+dy<len(arr[0]) and not visited[x+dx][y+dy]:
                helper(arr, x+dx,y+dy, word, visited, words, dic)
                #word = word[:-1]
        word=word[:-1]
        #print word
        #arr[x][y]=tmp
        visited[x][y]=False

    t=Trie()
    for w in dictionary:
        t.insert(w)

    words = set()

    for x in range(len(arr)):
        for y in range(len(arr[0])):
            if t.find(arr[x][y]):
                helper(arr,x,y, "", visited, words, dictionary)
                print ("words:",words)
                print ("new line:")
                max_num=max(max_num, len(words.intersection(dictionary)))
    return max_num

arr=[
    ['e', 'a', 'n','x'],
    ['t', 't', 'i','o'],
    ['a', 'r', 'a','z']
]

dic=set(['eat', 'rain', 'in', 'rat' ])

print (maxPackedWords(arr, dic))