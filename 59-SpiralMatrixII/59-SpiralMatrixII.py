
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        size1 = n*n
        top = 0
        bottom = n-1
        left= 0 
        right = n-1
        j = 1
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        while(left <=right and top <=bottom and j<=size1):
            for i in range(left, right+1):
                matrix[top][i] = j
                j +=1
            
            top +=1
            for i in range(top, bottom+1):
                matrix[i][right] = j
                j+=1
            
            right-=1

            if (left <=right and j <=size1):
                for i in range(right, left-1, -1):
                    matrix[bottom][i] = j
                    j+=1

                bottom-=1

            if (top <=bottom  and j<=size1):
                for i in range(bottom, top-1, -1):
                    matrix[i][left] = j
                    j+=1
                
                left +=1
        
        return matrix
            



            

