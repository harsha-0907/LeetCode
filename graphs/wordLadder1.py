# Word-Ladder

def wordLadder(beginword, endword, wordList):
    def dfs(target, wordList, distance, l):
        #print(target)
        for __ in range(len(wordList)):
            word = wordList[__]
            cnt = 0
            for i in range(length):
                if word[i] != target[i]:
                    cnt += 1
                if cnt == 2:
                    break
            
            if cnt == 1:
                print(target, word)
                if word == endword:
                    print(l)
                    if min_distance[0] == 0 or min_distance[0] > distance + 2:
                        min_distance[0] = distance + 2
                else:
                    dfs(word, wordList[:__]+wordList[__+1:], distance+1, l + [target])
        return None


    min_distance = [0]
    if endword not in wordList or endword == beginword:
        return min_distance[0]
    length = len(beginword)
    dfs(beginword, wordList, 0,[])
    return min_distance[0]
    
def optimizedWordLadder(beginWord: str, endWord: str, wordList) -> int:
    queue = [beginWord]; list1 = []; distance = 0; length = len(beginWord)
    if endWord not in wordList:
        return distance
    while queue != []:
        node = queue.pop(0)
        if node in wordList:
            wordList.remove(node)
        for nword in wordList:
            cnt_ = 0
            for i in range(length):
                if nword[i] != node[i]:
                    cnt_ += 1
                if cnt_ == 2:
                    break
            else:
                if cnt_ == 1:
                    if endWord == nword:
                        return distance + 2
                    else:
                        list1.append(nword)
        if queue == []:
            queue = list(set(list1)); list1 = []
            distance += 1
    return 0

beginword = "hit"; endword = "cog"; wordList = ["hot","dot","dog","lot","log"]
res = optimizedWordLadder(beginword, endword, wordList)
print(res)