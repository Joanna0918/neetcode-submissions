class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self.root

        def dfs(curr, start):
            if start == len(word) - 1:
                if word[start] in curr.children:
                    return curr.children[word[start]].isEnd
                elif word[start] == ".":
                    for trieNode in curr.children.values():
                        if trieNode.isEnd:
                            return True
                    return False
                else:
                    return False
            
            else:
                if word[start] in curr.children:
                    return dfs(curr.children[word[start]], start + 1)
                elif word[start] == ".":
                    for trieNode in curr.children.values():
                        if dfs(trieNode, start + 1):
                            return True
                    return False
                else:
                    return False
        
        return dfs(curr, 0)
