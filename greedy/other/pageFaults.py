# Here we will be implementing the paging process of LRU (Least Recently Used caching process)

def leastRecentlyUsed(pages, max_size):
    """ Implementation of the least recently used paging mechanism"""
    # Return the number of page faults that have occured
    number_of_pages = len(pages)
    dict1 = dict(); page_faults = 0; ed = 0 # The element to be removed
    
    for page in pages:
        if page in dict1:
            # No page faults occur
            dict1[page] += 1
            
        else:
            if len(dict1) == c:
                # The size of the stack is full
                # Remove the last element
                while dict1[pages[ed]] != 1:
                    dict1[pages[ed]] -= 1
                    ed += 1
                del(dict1[pages[ed]]); ed += 1

            dict1[page] = 1; page_faults += 1
        
    return page_faults

jobs = [5, 0, 1, 3, 2, 4, 1, 0, 5]
c = 4

res = leastRecentlyUsed(jobs, c)

print(res)