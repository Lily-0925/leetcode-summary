class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        visited = [None for i in range(n)]
        for i in range(n):
            if visited[i] == None:
                if not self.dfs(visited,i,1,graph):
                    return False
        return True

    def dfs(self,visited,i,flag,graph):
        if visited[i] != None:
            return visited[i] == flag
        visited[i] = flag
        for num in graph[i]:
            if not self.dfs(visited,num,-flag,graph):
                return False
        return True