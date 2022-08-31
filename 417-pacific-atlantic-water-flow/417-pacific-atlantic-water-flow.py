class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n = len(heights), len(heights[0])
        
        def bfs(vis):
            que = deque(vis)
            while que:
                i, j = que.popleft()
                 
				# Go through cells adjacent to the current cell at (i, j)
                for newI, newJ in ((i,j+1), (i+1,j), (i-1,j), (i,j-1)):
					# check new coords are in range and that the next cell's height is >= cur cell's height
					# (since we are searching from the ocean)
                    if 0 <= newI < m and 0 <= newJ < n and (newI, newJ) not in vis and heights[newI][newJ] >= heights[i][j]:
                        que.append((newI, newJ))
                        vis.add((newI, newJ))

        
        # Add initial tiles for each ocean
        pacVisited = set([(i, 0) for i in range(m)]) | set([(0, i) for i in range(n)])
        atVisited = set([(m - 1, i) for i in range(n)]) | set([(i, n - 1) for i in range(m)])
        
        # do bfs for each ocean
        bfs(pacVisited)
        bfs(atVisited)
        
        # take intersection of two visited
        return pacVisited & atVisited