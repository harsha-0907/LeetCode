# To find the longest prefix between 2 lists of numbers

def longestCommonPrefix(list1, list2):
    set1 = set()
    for ele in list1:
        ele = str(ele);n = ""
        for pos in ele:
            n += pos
            set1.add(n)
    
    maxsize = 0
    for ele in list2:
        ele1 = str(ele); n = ""
        for pos in ele1:
            n += pos
            if n in set1:
                maxsize = max(len(n), maxsize)
    
    return maxsize

list1 = [1,10,100]; list2 = [1000]

print(longestCommonPrefix(list1, list2))