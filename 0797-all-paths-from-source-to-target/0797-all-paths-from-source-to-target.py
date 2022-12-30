class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        #edge case
        if not graph:
            return []
        
        # build the graph with dict
        d = {}
        for i in range(len(graph)):
            d[i] = graph[i]
        
        
        n = len(graph)
        stack = [(0, [0])]
        res = []
        
        while stack:
            node, path = stack.pop()
            
            if node == n-1:
                res.append(path)
            
            for nei in d[node]:
                stack.append((nei, path+[nei]))
        
        return res