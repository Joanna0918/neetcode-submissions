class Node:
    def __init__(self, val, is_end):
        self.val, self.is_end = val, is_end
        self.children = {}

class PrefixTree:

    def __init__(self):
        self.root = Node(0, False)

    def insert(self, word: str) -> None:
        curr = self.root
        for i in range(len(word)):
            if word[i] not in curr.children:
                curr.children[word[i]] = Node(word[i], i == len(word) - 1)
            curr = curr.children[word[i]]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for i in range(len(word)):
            if word[i] in curr.children:
                curr = curr.children[word[i]]
            else:
                return False
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in range(len(prefix)):
            if prefix[i] in curr.children:
                curr = curr.children[prefix[i]]
            else:
                return False
        return True