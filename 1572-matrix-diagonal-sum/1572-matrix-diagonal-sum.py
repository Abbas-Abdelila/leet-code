class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        for idx, row in enumerate(mat):
            total += row[idx]

        i = len(mat)-1
        for col in zip(*mat):
            total += col[i]
            i -= 1
        
        if len(mat)%2 == 0:
            return total
        else:
            mid = len(mat)//2
            return total - mat[mid][mid]
