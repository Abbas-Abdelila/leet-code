class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        lands = deque([
            (i, j) for i in range(m) for j in range(n) if grid[i][j] == 1
        ])
        if len(lands) == m * n or len(lands) == 0:
            return -1
        directions = [
            (1,0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]
        level = 0
        while lands:
            size = len(lands)
            for _ in range(size): 
                i, j = lands.popleft()
                for x, y in directions:
                    xi, yj = x+i, y+j
                    if 0 <= xi < m and 0 <= yj < n and grid[xi][yj] == 0:
                        lands.append((xi, yj))
                        grid[xi][yj] = 1
            level += 1
        return level - 1