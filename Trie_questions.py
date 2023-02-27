'''

'''

class TrieNode():

    def __init__(self):
        self.isLeaf = False
        #self.char = char
        self.children = {}

class Trie():
    def __init__(self):
        self.root = TrieNode()
        self.ouput=[]# used to store all words containing a searching prefix

    def insert(self, word):
        node = self.root
        for ch in word: #ch single char
            if not ch in node.children:
                node.children[ch]=TrieNode()
            node=node.children[ch]

        #after a word is inserted, set current node's isLeaf=True
        node.isLeaf = True

    def find(self, word): # check if a word (maybe a prefix of another word) is in Trie
        node = self.root

        for ch in word:
            if not ch in node.children:
                return False
            node = node.children[ch]
        return True

    def search_all_prefix(self, word):
        node = self.root
        #print "search word:: ",word
        #first navigate to last node of word
        for ch in word:
            if ch in node.children:
                node = node.children[ch]
            else:
                #not found entire word, return []
                return []
        self.ouput =[]
        self.dfs(node, word)#[:-1])#word[:-1] = word[0:len(word)-1]

        #return self.ouput if len(self.ouput)<=3 else self.ouput[0:3]

        return self.ouput #if len(self.ouput) <= 3 else self.ouput[0:3]


    def dfs(self, node, pre):
        if node.isLeaf:
            self.ouput.append(pre)

        for ch, child_node in node.children.items():
            self.dfs(child_node, pre+ch)
        pre=pre[0:-1]

    def count_all_prefix(self, word):
        return len(self.search_all_prefix(word))

'''
tr=Trie()
tr.insert("here")
tr.insert("hear")
tr.insert("he")
tr.insert("hello")
tr.insert("how ")
tr.insert("her")
tr.insert("the")
tr.insert("person")
tr.insert("poor")

print tr.search_all_prefix("he")
print tr.find("her")
print tr.find("hepp")
print tr.search_all_prefix("He")
print tr.count_all_prefix("he")
print tr.search_all_prefix("pe")
'''

tr=Trie()
products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
for p in products:
    tr.insert(p)

print ("searchWord:")
for i in range(1,len(searchWord)+1):
    #print searchWord[0:i]
    print ("prefix? ",searchWord[0:i], tr.search_all_prefix(searchWord[0:i]))
