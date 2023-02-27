'''
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node
n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge
 from node i to node graph[i][j]).



Example 1:


Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
Example 3:

Input: graph = [[1],[]]
Output: [[0,1]]
Example 4:

Input: graph = [[1,2,3],[2],[3],[]]
Output: [[0,1,2,3],[0,2,3],[0,3]]
Example 5:

Input: graph = [[1,3],[2],[3],[]]
Output: [[0,1,2,3],[0,3]]
'''

#accepted by leetcode
class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """

        ans = []
        visited = [False] * len(graph)

        def DFS(graph, start, end, visited, med):
            if start == end:
                med.append(start)
                ans.append(list(med))
                # return #can't return here
            else:
                med.append(start)
                visited[start] = True
                for neighbor in graph[start]:
                    if not visited[neighbor]:
                        DFS(graph, neighbor, end, visited, med)
            med.pop()
            visited[start] = False

        n = len(graph)
        DFS(graph, 0, n - 1, visited, [])
        return ans
o=Solution()
graph = [[1,2],[3],[3],[]]

print (o.allPathsSourceTarget(graph))
graph =[[4,3,1],[3,2,4],[3],[4],[]]
print (o.allPathsSourceTarget(graph))