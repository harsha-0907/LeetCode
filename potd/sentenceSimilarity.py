# To find if the string is similar or not

def sentenceSimilarity(sentence1, sentence2):
    # The bigger string will be considered as sentence1
    if len(sentence2) > len(sentence1):
        return sentenceSimilarity(sentence2, sentence1)
    
    sentence1 = list(sentence1.split()); sentence2 = list(sentence2.split())

    low = 0; high = len(sentence2) - 1

    for word in sentence2:
        if word == sentence1[low]:
            low += 1
        else:
            break
    if low == 0:
        return False
    elif low == len(sentence2):
        return True
    
    
    print("Not completely right")
    
    i = 1
    while high > low:
        word = sentence1[-i]
        word2 = sentence2[high]
        if word2 != word:
            return False
        i += 1; high -= 1
    
    if high == low:
        return True
    
    return False


def areSentencesSimilar(st1, st2):
    l1, l2 = len(st1), len(st2)
    if l2 > l1:
        return self.areSentencesSimilar(st2, st1)

    st1, st2 = list(st1.split()), list(st2.split())
    l1, l2 = len(st1), len(st2)

    # Checked for the test cases where the string2 lies at the edges
    if st1[:l2] == st2 or st1[-l2:] == st2:
        return True
        
    low = 0
    while st1[low] == st2[low]:
        low += 1
        
    print(low)
        
    i = 1
    while st1[l1-i] == st2[l2-i] and l2 - i >= low:
        i += 1
        
    if low == l2-i+1:
        return True
    return False



sentence1 = "of"
sentence2 = "A lot of words"

res = areSentencesSimilar(sentence1, sentence2)

print(res)
