class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        R = len(board)
        C = len(board[0])
        
        next_board = [[False]*C for _ in range(R)]
        
        
        def count(x,y):
            total = 0
            for dx in range(-1, 1 + 1):
                nx = x + dx
                if not (0 <= nx < R):
                    continue
                
                for dy in range(-1, 1 + 1):
                    if (dx==0 and dy==0):
                        continue
                    
                    ny = y + dy
                    if not (0 <= ny < C):
                        continue
                    
                    if(board[nx][ny]==1):
                        total += 1
            return total
            
        
        
        for x in range(R):
            for y in range(C):
                c = count(x,y)
                
                if(board[x][y]==1):
                    if(c < 2):
                        next_board[x][y] = False
                    elif (2 <= c <= 3):
                        next_board[x][y] = True
                    else: 
                        next_board[x][y] = False
                
                else:
                    if(c==3):
                        next_board[x][y] = True
                    else:
                        next_board[x][y] = False
                        
                        
        for x in range(R):
            for y in range(C):
                if next_board[x][y]:
                    board[x][y] = 1
                else:
                    board[x][y] = 0
                        
                        
                        
                
            