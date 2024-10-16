# To create a longest happy string

def createLongestHappyString(a, b, c):
    def getmax(dict1, ex=[]):
        ele = None; maxi = 0
        for i in dict1 :
            if dict1[i] > maxi and i not in ex:
                ele = i
                maxi = dict1[i]
        return ele
            
    answer = ""
    dict1 = {'a': a, 'b':b, 'c':c}
    for pos in range(a+b+c):
        ele = getmax(dict1)
        if len(answer) < 2:
            answer += ele
            dict1[ele] -= 1
        else:
            if answer[-2:]+ele == 'aaa' or answer[-2:]+ele == 'bbb' or answer[-2:]+ele == 'ccc':
                ele = getmax(dict1, [ele])
                if not ele:
                    # NO element exists
                    return answer
            
            answer += ele
            dict1[ele] -= 1
    return answer
            
    
a = 7
b = 0
c = 1

res = createLongestHappyString(a,b,c)

print(res)                    