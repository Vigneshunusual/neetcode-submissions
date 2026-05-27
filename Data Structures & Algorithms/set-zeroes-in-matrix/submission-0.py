class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        m=len(matrix[0])
        row=set()
        col=set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    row.add(i)
                    col.add(i)
        for i in range(n):
            for j in range(m):
                if i in row or j in col:
                    matrix[i][j]=0
        
        