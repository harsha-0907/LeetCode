# To find the smallest number of chairs required for a party
from collections import deque
import heapq

def calculateMinChairs(persons, target):
    """ Calulate the chair the 'target' person site in"""
    length = len(persons)
    start = [(persons[pos][0], pos) for pos in range(length)]
    end = [(persons[pos][1], pos) for pos in range(length)]
    chairs = dict(); empty_chairs = []
    start[:] = sorted(start, key = lambda x: x[0])
    end[:] = sorted(end, key = lambda x: x[0])
    
    pos = end_pos = max_chairs = 0
    
    while pos < length:
        # Until the user is the required user
        st, ed = start[pos][0], end[end_pos][0]
        new_person, exit_person = start[pos][1], end[end_pos][1]
        if st < ed:
            # Here learn that the intent of arranging chair to the person in more important than taking someone's
            # If the end is greater than the starting it means that a person is entering
            if empty_chairs == []:
                # There are no empty chairs
                chairs[new_person] = max_chairs
                max_chairs += 1
            else:
                # There are empty chairs available
                chair = heapq.heappop(empty_chairs)
                chairs[new_person] = chair
            pos += 1
            if new_person == target:
                return chairs[new_person]
            
        else:
            # If the start is greater than the starting
            # A person is exiting
            empty_chair = chairs[exit_person]
            heapq.heappush(empty_chairs, empty_chair)
            del(chairs[exit_person])
            end_pos += 1
    return -1

persons = [[18,19],[10,11],[21,22],[5,6],[2,3],[6,7],[43,44],[48,49],[53,54],[12,13],[20,21],[34,35],[17,18],[1,2],[35,36],[16,17],[9,10],[14,15],[25,26],[37,38],[30,31],[50,51],[22,23],[3,4],[27,28],[29,30],[33,34],[39,40],[49,50],[15,16],[4,5],[46,47],[51,52],[32,33],[11,12],[28,29],[47,48],[36,37],[40,41],[42,43],[52,53],[41,42],[31,32],[23,24],[8,9],[19,20],[24,25],[26,27],[45,46],[44,45],[7,8],[13,14],[38,39]]

res = calculateMinChairs(persons, 1)

print(res)
    