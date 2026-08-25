class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str = encoded_str + str(len(s)) + '#' + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded_list = []

        while i < len(s)-1:
            j = i+1
            while s[j] != '#':
                j += 1
            size = int(s[i:j])
            word = s[j+1:j+1+size]
            decoded_list.append(word)
            i = j+1+size
        
        return decoded_list
