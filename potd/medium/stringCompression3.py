# To perform string compression by using given methods

class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""; prev = word[0]; cnt = 1
        length = len(word)
        for pos in range(1, length):
            ch = word[pos]
            if cnt > 8:
                comp += f"9{word[pos-1]}"
                cnt = 0; prev = word[pos]
            if ch == prev:
                cnt += 1
            else:
                comp += f"{cnt}{word[pos-1]}"
                cnt = 1; prev = word[pos]
        comp += f'{cnt}{word[-1]}'
        return comp