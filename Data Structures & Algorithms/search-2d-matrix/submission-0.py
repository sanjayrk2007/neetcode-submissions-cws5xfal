class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS=len(matrix)
        COLS=len(matrix[0])
        for i in range(ROWS):
            for j in range(COLS):
                if(matrix[i][j]==target):
                    return True
        return False