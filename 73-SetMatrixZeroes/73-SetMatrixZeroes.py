class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_num = set()
        col_num = set()
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row_num.add(i)
                    col_num.add(j)
        print(row_num,col_num)

        for i in range(m):
            if i in row_num:
                matrix[i]=[0]*n
                print(matrix)
            for j in range(n):
                if j in col_num:
                    matrix[i][j] = 0
