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
    
def optimizedWordLadder(self, begin_word: str, end_word: str, word_list: List[str]) -> int:
    
    return 0

beginword = "hit"; endword = "cog"; wordList = ["hot","cog","dot","dog","hit","lot","log"]
res = wordLadder(beginword, endword, wordList)
print(res)