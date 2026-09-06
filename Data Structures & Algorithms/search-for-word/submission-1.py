class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set()

        def backtrack(r, c, level):
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or (r, c) in seen:
                return False

            if board[r][c] == word[level] and level == len(word) - 1:
                return True

            if board[r][c] != word[level]:
                return False

            seen.add((r, c))
            found = (backtrack(r + 1, c, level + 1)
                    or backtrack(r - 1, c, level + 1)
                    or backtrack(r, c + 1, level + 1)
                    or backtrack(r, c - 1, level + 1))
            seen.remove((r, c))
            return found           
        
        level = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, level):
                    return True
        return False