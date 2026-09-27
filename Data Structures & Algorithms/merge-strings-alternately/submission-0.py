class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1, n2 = len(word1), len(word2)
        w1, w2 = 0, 0
        res = ""

        while True:
            if w1 >= n1:
                res += word2[w2:]
                break
            if w2 >= n2:
                res += word1[w1:]
                break
            
            res = res + word1[w1] + word2[w2]
            w1 += 1
            w2 += 1
        
        return res