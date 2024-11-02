class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        length = len(words)
        for pos in range(length):
            pword = words[pos-1]; word = words[pos]
            if pword[-1] != word[0]:
                return False
        
        return True
