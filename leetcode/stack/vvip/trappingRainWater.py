# Trapping the Rain Water 

def trapWater(heights):
    total_water = 0; removable_size = 0
    stack = [(heights[0], 0, 0)]
    for x2 in range(len(heights)):
        h2 = heights[x2]
        if h2 <= heights[x2]:
            removable_size += h2
        else:
            h1, x1, removable_size1 = stack[-1]
            while stack and stack[-1][0] < h2:
                hnew, xnew, remnew = stack.pop()
                if h1 <= hnew:
                    h1, x1, removable_size1 = hnew, xnew, remnew
            
            if stack:
                # It means there is an element of height >= h2
                if stack[-1][0] == h2:
                    # They are same height
                    quantity = (h2 * (x2 - x1 - 1)) - stack[-1][2]
                    stack[-1][1], stack[-1][2] = x2, removable_size + quantity
                else:
                    quantity = (min(h2, stack[-1][0]) * (x2 - stack[-1][1] - 1)) - (removable_size)
            
            removable_size += removable_size1
            total_water += quantity
            
                    

    return total_water

heights = [0,1,0,2,1,0,1,3,2,1,2,1]

res = trapWater(heights)

print(res)