class Solution:
    def isValidSudoku(self, board) -> bool:
        # Rows
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[i][j]
                if item in s:
                    return False
                elif item != '.':
                    s.add(item)
        
        # Columns
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[j][i]
                if item in s:
                    return False
                elif item != '.':
                    s.add(item)

        # Box
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                s = set()
                for i in range(3):
                    for j in range(3):
                        item = board[box_row + i][box_col + j]
                        if item in s:
                            return False
                        elif item != '.':
                            s.add(item)

        return True




obj = Solution()
print(obj.isValidSudoku(board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))