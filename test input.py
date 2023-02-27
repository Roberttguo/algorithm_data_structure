import os
import sys

#loop = int(raw_input())

m = {}


def add_word(word):
    for i in range(1, len(word) + 1):
        if word[:i] in m:
            m[word[:i]] += 1
        else:
            m[word[:i]] = 1


def find_partial(word):
    return m.get(word) or 0

add_word("abcd")
print m
print "partial:", find_partial("ab")

'''
for i in range(loop):
    input = raw_input().split()
    if input[0] == "add":
        add_word(input[1])
    else:
        print find_partial(input[1])
'''

'''        
def contacts(queries):
    for query in queries:
        print type(query)
        print query
        s1, s2 = query
        print "s1 and s2: ", s1, s2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    queries_rows = int(raw_input().strip())

    queries = []

    for _ in xrange(queries_rows):
        queries.append(raw_input().rstrip().split())

    result = contacts(queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
'''