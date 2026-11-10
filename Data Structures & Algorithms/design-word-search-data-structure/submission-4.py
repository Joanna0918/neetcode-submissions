class TrieNode:

    def __init__(self):
        self.isWord = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                cNode = TrieNode()
                curr.children[c] = cNode
            curr = curr.children[c]
        curr.isWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        
        def dfs(i, curr):
            if i == len(word):
                return curr.isWord

            if word[i] == ".":
                for char in curr.children:
                    if dfs(i + 1, curr.children[char]):
                        return True
                return False
            elif word[i] not in curr.children:
                return False
            elif word[i] in curr.children:
                return dfs(i + 1, curr.children[word[i]])
        
        return dfs(0, curr)