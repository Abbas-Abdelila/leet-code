class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m,n = len(heights),len(heights[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]#right,left,up,down
        visited = set()
        output = 0
        heap = [(0,0,0)]#minimum threshold, x, y

        while heap:
            #print(heap)
            k,x,y = heappop(heap) #heappop() gives us the minimum value from the heap.
            #print(k,x,y)
            output = max(output,k)
            #print(k,x,y,output)
            if (x,y) == (m-1,n-1):
                return output
            visited.add((x,y))#adding the co-ordinates to the set so that we don't visit them again.
            for dx,dy in dirs:
                #(dx,dy,"0")
                new_x,new_y = x+dx,y+dy
                #print(new_x,new_y,"1")
                if 0<=new_x<m and 0<=new_y<n and (new_x,new_y) not in visited:#check if new_x,new_y are in bounds and aren't repeated.
                    new_k = abs(heights[x][y] - heights[new_x][new_y])
                    #print(heights[x][y],heights[new_x][new_y],new_k ,"2")
                    heappush(heap,(new_k,new_x,new_y))
        return -1