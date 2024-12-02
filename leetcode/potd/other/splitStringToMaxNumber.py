# To split a string into maximum number of unique subsrtings

# This is the greedy approach
def maxSubstrings(string: str):
    # To find the maximum number of substrings by splitting the string
    def splitString(string, completed=set()):
        if string == "":
            return len(completed)
        substr = ""
        for i in range(len(string)):
            substr += string[i]
            if substr not in completed:
                completed.add(substr)
                return splitString(string[i+1:], completed)
        if string not in completed:
            return len(completed)+1
        else:
            return len(completed)
        
    return splitString(string)

# This is the backtracking approach (kind of dp)
def maxSubstrings1(string):
    def backTracking(string, set1, pos, substr):
        if len(string) == pos:
            # For the last element return the number of unique elements
            if substr not in set1 and substr != "":
                return len(set1) + 1
            else:
                return len(set1)
        else:
            substr += string[pos]
            if substr in set1:
                return backTracking(string, set1, pos+1, substr)
            else:
                return max(backTracking(string, set1, pos+1, substr), backTracking(string, set1 + [substr], pos+1, ""))
    
    return backTracking(string, [], 0, "")
    
string = "wwwzfvedwfvhsww"
result = 11

res = maxSubstrings1(string)

print(res)