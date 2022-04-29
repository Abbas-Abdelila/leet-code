class Solution:
    BLUE = -1
    WHITE = 0
    GREEN = 1
    
    @staticmethod
    def getOppositeColor(color: int) -> int:
        return color * -1
    
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [self.WHITE] * n
        
        for i in range(n):
            if colors[i] != self.WHITE:
                continue
                
            colors[i] = self.BLUE
            queue = deque()
            queue.append((i, self.BLUE))
            while len(queue) > 0:
                node, color = queue.popleft()
                oppositeColor = self.getOppositeColor(color)
                for child in graph[node]:
                    if colors[child] == color:
                        return False
                    
                    if colors[child] == oppositeColor:
                        continue
                    
                    colors[child] = oppositeColor
                    queue.append((child, oppositeColor))
                    
        return True
        