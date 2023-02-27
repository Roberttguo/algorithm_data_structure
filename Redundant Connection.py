'''
Leetcode 684
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added.
The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is
represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai
and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers,
 return the answer that occurs last in the input.



Example 1:

1---2
\  /
 \/
 3
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]

 2---1---5
 |   |
 |   |
 3---4

 Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
'''

#following is accepted on 2/6/2022
#idea is as build a graph, check if last added edge can form cicle or loop by checking if there is path between vertic u,v
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # build graph
        graph = {}
        N = len(edges)

        def hasPath(graph, start, end, visited):
            if len(graph) == 0 or start not in graph:
                return False
            visited.add(start)
            if start == end:
                return True

            for nbr in graph[start]:
                if nbr not in visited:
                    if hasPath(graph, nbr, end,visited):# import this line, cannot 'return hasPath(graph, nbr,end, visited)' directly here'
                        return True
            return False

        for i in range(N):
            start = edges[i][0]
            end = edges[i][1]
            visited = set()
            if hasPath(graph, start, end, visited):
                return edges[i]

            if start in graph: #gradually build graph from edges 0 to N-1, then can find last added edge that could form a cicle/loop
                graph[start].append(end)
            else:
                graph[start] = [end]
            if end in graph:
                graph[end].append(start)
            else:
                graph[end] = [start]

        return []
