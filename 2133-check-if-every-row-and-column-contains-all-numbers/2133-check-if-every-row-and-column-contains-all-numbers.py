class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        rows = [row for row in matrix]
        cols = [col for col in zip(*matrix)]
        one_to_n = [i for i in range(1, len(matrix)+1)]
        
        for row in matrix:
            if len(row) != len(set(row)):
                return False
            for num in row:
                if num not in one_to_n:
                    return False
                
        for col in zip(*matrix):
            if len(col) != len(set(col)):
                return False
            for num in col:
                if num not in one_to_n:
                    return False
        
        return True