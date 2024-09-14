# Dis-Joint set (Union-Find) in a graph

def find(arr, num):
    # Code here
    if arr[num-1] != num:
        return find(arr, arr[num-1])
    else:
        return num

# function shouldn't return or print anything
def unionSet(A, X, Z):
    # Code here
    pu=find(A,X)
    pv= find(A,Z)
    
    A[pu-1]=pv

