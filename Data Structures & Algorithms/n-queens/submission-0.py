class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result=[]
        board=[["."]*n for _ in range(n)]
        cols=set()
        posdiag=set()
        negdiag=set()
        def backtrack(row):
            if row==n:
                copy=["".join(r) for r in board]
                result.append(copy)
                return
            for col in range(n):
                if col in cols or (row+col) in posdiag or (row-col) in negdiag:
                    continue
                board[row][col]="Q"
                cols.add(col)
                posdiag.add(row+col)
                negdiag.add(row-col)
                backtrack(row+1)
                cols.remove(col)
                posdiag.remove(row+col)
                negdiag.remove(row-col)
                board[row][col]="."
        backtrack(0)
        return result