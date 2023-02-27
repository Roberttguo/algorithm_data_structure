'''
Kitty has a tree, , consisting of  nodes where each node is uniquely labeled from  to . Her friend Alex gave her  sets,
where each set contains  distinct nodes. Kitty needs to calculate the following expression on each set:
where:

 denotes an unordered pair of nodes belonging to the set.
 denotes the number of edges on the unique (shortest) path between nodes  and .
Given  and  sets of  distinct nodes, calculate the expression for each set. For each set of nodes, print the value of
the expression modulo  on a new line.

Example

edges=[[1,2],[1,3],[1,4], [3,5],[3,6],[3,7]]
queries=[4,5,7]
      5
      |
   6<-3->7
      |
   2--1--->4

There are three pairs that can be created from the query set: . The distance from  to  is , from  to  is , and from  to  is .

Now do the summation:

'''

class Solution(object):
    def __init__(self, edges):
        self.graph={}
        for e in edges:
            if e[0] in self.graph:
                self.graph[e[0]].append(e[1])
            else:
                self.graph[e[0]]=[e[1]]
            if e[1] in self.graph:
                self.graph[e[1]].append(e[0])
            else:
                self.graph[e[1]]=[e[0]]
        print self.graph

    def BFS(self, start, end, steps, dist, visited):
        if start==end:
            dist[0]=min(dist[0], steps)
            return
        visited.add(start)

        for next in self.graph[start]:
            if next not in visited:
                self.BFS(next, end, steps+1, dist, visited)
        visited.remove(start)

    def shortestDist(self, start, end):
        dist=[2**32]
        visited=set()
        self.BFS(start,end, 0, dist, visited )
        return dist[0]

    def combination(self, arr, k):
        res=[]
        tmp=[]
        def helper(arr, start, k, tmp, res):
            if k==0:
                res.append(list(tmp))
                return
            for i in range(start, len(arr)):
                tmp.append(arr[i])
                helper(arr,i+1, k-1, tmp, res)
                tmp.pop()
        helper(arr,0, k,tmp, res)
        return res
    def totSum(self, queries):
        all=self.combination(queries, 2)
        tot=0
        mod=10**9+7
        for pair in all:
            dist=self.shortestDist(pair[0], pair[1])
            prod=pair[0]*pair[1]*dist
            tot+=prod
        print "Total sum: ", tot
        return tot%mod

edges=[[1,2],[1,3],[1,4], [3,5],[3,6],[3,7]]
queries=[4,5,7]

s=Solution(edges)
print s.shortestDist(4,5)
print s.shortestDist(2,1)
print s.shortestDist(5,7)
print s.shortestDist(2,6)
print s.shortestDist(4,7)
print s.combination(queries, 2)
print s.totSum(queries)