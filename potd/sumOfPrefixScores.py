# Sum of prefix scores of strings
from collections import deque

def sumOfScores(strings):
    dict1 = dict(); dict2 = dict()
    for string in strings:
        s = ""
        if string not in dict2:
            dict2[string] = set()
            
        for ch in string:
            s += ch; dict2[string].add(s)
            if s not in dict1:
                dict1[s] = 1
            else:
                dict1[s] += 1
    ans = []
    #print(dict1)
    #print(dict2)
    for string in strings:
        tot = 0
        for ch in dict2[string]:
            #print(ch, )
            tot += dict1[ch]
        ans.append(tot)
    return ans

strings = ["abc","ab","bc","b"]

res = sumOfScores(strings)

print(res)


        
