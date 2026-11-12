class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        curr = self
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)

        ROWS, COLS = len(board), len(board[0])
        neighbors = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited, res = set(), set()
        
        def dfs(r, c, node, word):
            if (r >= ROWS or c >= COLS or r < 0 or c < 0 
                or (r, c) in visited
                or board[r][c] not in node.children):
                return

            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)
            for dr, dc in neighbors:
                dfs(r + dr, c + dc, node, word)
            visited.remove((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        return list(res)