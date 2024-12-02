# To seperate the white and black balls 

def seperateBalls(balls):
    # 1 - black , 0 - White
    # Black balls will be arranged to the left
    tot_pos_shift = 0; cnt = 0
    for pos in range(len(balls)):
        if balls[pos] == '0':
            tot_pos_shift += (pos - cnt)
            cnt += 1
    
    return tot_pos_shift

balls = "100"

res = seperateBalls(balls)

print(res)