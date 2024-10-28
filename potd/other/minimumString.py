# To find the length of the string after removing all occurences of 'AB' and 'CD'

def minimumString(string):
    i = 0
    while i < len(string)-1:
        if string[i:i+2] == 'AB' or string[i:i+2] == 'CD':
            print(string)
            string = string[:i] + string[i+2:]
            print(i)
            i = max(0, i-1)
        else:
            i += 1
    
    print(string)
    return len(string)

string = "ABFCACDB"

res = minimumString(string)

print(res)