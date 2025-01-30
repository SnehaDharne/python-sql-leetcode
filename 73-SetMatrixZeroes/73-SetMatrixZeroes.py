class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # row_num = set()
        # col_num = set()
        # m = len(matrix)
        # n = len(matrix[0])
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == 0:
        #             row_num.add(i)
        #             col_num.add(j)
        # print(row_num,col_num)

        # for i in range(m):
        #     if i in row_num:
        #         matrix[i]=[0]*n
        #         print(matrix)
        #     for j in range(n):
        #         if j in col_num:
        #             matrix[i][j] = 0


        m = len(matrix)
        n = len(matrix[0])
        col0 = 1

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    if j!=0:
                        matrix[0][j] = 0
                    else:
                        col0 = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] != 0:
                    if matrix[i][0] == 0 or matrix[0][j] == 0:
                        matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0
        if col0 == 0:
            for i in range(m):
                matrix[i][0] = 0

 
