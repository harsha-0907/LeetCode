# Word-Ladder-2

import time

def wordLadder2(beginWord, endWord, wordList):
    def dfs(visited, distance, ans):
        if min_distance[0] != 0 and distance+1 > min_distance[0]:
            return ans
        word = visited[-1]
        if word == endWord:
            if ans == dict() or distance+1 not in ans:
                ans = {distance+1: []}
            ans[distance+1].append(visited)
            min_distance[0] = distance + 1
            return ans
        
        for i in range(length):
            for ch in "abcedfghijklmnopqrstuvwxyz":
                nword = word[:i] + ch + word[i+1:]
                if nword not in visited and nword in wordList:
                    ans = dfs(visited + [nword], distance+1, ans)
        return ans

    result = []; min_distance = [0]; length = len(beginWord)
    stack = [beginWord]
    if endWord not in wordList:
        return []
    else:
        ans = dfs(stack, 0, dict())
        #print(ans)
    if ans != dict():
        return ans[min_distance[0]]

def optimizedWordLadder2(beginWord, endWord, wordList):
    def dfs(visited, distance, ans):
        if min_distance[0] != 0 and distance+1 > min_distance[0]:
            return ans
        word = visited[-1]
        if endWord == word:
            if min_distance[0] == 0 or (distance+1) not in ans:
                ans = {distance+1: []}
            ans[(distance+1)].append(visited)
            min_distance[0] = distance + 1
            return ans
        
        for i in range(length):
            for ch in "abcdefghijklmnopqrstuvwxyz":
                nword = word[:i] + ch + word[i+1:]
                if nword not in visited and nword in wordList:
                    ans = dfs(visited+tuple([nword]), distance+1, ans)
        return ans
    if endWord not in wordList:
        return []
    wordList = set(wordList)
    min_distance = [0]; length = len(beginWord)
    ans = dfs(tuple([beginWord]), 0, dict())
    if ans == dict():
        return []
    return ans[min_distance[0]]

t1 = time.time()
wordList = ["hot","dot","dog","lot","log","cog"]
beginWord = "hit"; endWord = "cog"
res = wordLadder2(beginWord, endWord, wordList)
t2 = time.time()
res = optimizedWordLadder2(beginWord, endWord, wordList)
t3 = time.time()
print(t2-t1, t3-t2)
print(res)
