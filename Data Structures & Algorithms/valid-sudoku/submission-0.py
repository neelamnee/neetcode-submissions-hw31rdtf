class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        grid = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9): 
                v = board[r][c]
                if v == ".":
                    continue 

                k = (r // 3) * 3 + (c // 3)
                if v in rows[r] or v in columns[c] or v in grid[k]:
                    return False 

                rows[r].add(v)
                columns[c].add(v)
                grid[k].add(v)

        return True
