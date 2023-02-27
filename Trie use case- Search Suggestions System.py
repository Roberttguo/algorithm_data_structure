'''
Given an array of strings products and a string searchWord. We want to design a system that suggests at most three
product names from products after each character of searchWord is typed. Suggested products should have common prefix
with the searchWord. If there are more than three products with a common prefix return the three lexicographically
minimums products.

Return list of lists of the suggested products after each character of searchWord is typed.



Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
Example 2:

Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
Example 3:

Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
Example 4:

Input: products = ["havana"], searchWord = "tatiana"
Output: [[],[],[],[],[],[],[]]


Constraints:

1 <= products.length <= 1000
There are no repeated elements in products.

All characters of products[i] are lower-case English letters.
1 <= searchWord.length <= 1000
All characters of searchWord are lower-case English letters.
'''

#accepted on 10/10/2021
class TrieNode():
    def __init__(self):
        self.isleaf = False
        self.children = {}


class Trie():
    def __init__(self):
        self.root = TrieNode()
        self.prefix = []

    def add(self, word):
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isleaf = True

    def find_all_prefix(self, pre):
        # find laste layer for pre first
        node = self.root

        for ch in pre:
            if ch in node.children:
                node = node.children[ch]
            else:
                return []
        self.prefix = []  # required to initialize here
        self.DFS(node, pre)
        return self.prefix

    def DFS(self, node, pre):
        if not node:
            return
        if node.isleaf:
            self.prefix.append(pre)
        for key, childnode in node.children.items():
            self.DFS(childnode, pre + key)
        # backtracking
        pre = pre[0:-1]


class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        ans = []
        T = Trie()
        for p in products:
            T.add(p)

        for i in range(1, len(searchWord) + 1):
            res = T.find_all_prefix(searchWord[0:i])
            res.sort()
            ans.append(res[0:3])
        return ans