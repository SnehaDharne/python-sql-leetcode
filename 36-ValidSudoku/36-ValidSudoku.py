def gotcha(arr):
    arr = [x for x in arr if x != '.']
    arr_set = set(arr)
    flag = len(arr_set) == len(arr)
    print(arr_set)
    print(arr)
    return flag

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            flag = gotcha(board[i])
            if not flag:
                return False
        for i in range(9):
            elements = [row[i] for row in board]
            flag = gotcha(elements)
            if not flag:
                return False
        for i in range(0, 9, 3):  
            for j in range(0, 9, 3):  
                elements = []
                for row in range(i, i + 3): 
                    for col in range(j, j + 3):  
                        elements.extend(board[row][col])

                flag = gotcha(elements)
                if not flag:
                    return False

        
        return True
                

