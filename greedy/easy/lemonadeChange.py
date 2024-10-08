# Solution for the lemonade change problem

def lemonadeChange(bills):
    n5 = n10 = n20 = 0
    for bill in bills:
        if bill == 5:
            n5 += 1
            continue
        elif bill == 10 and n5 > 0:
            n5 -= 1; n10 += 1
        elif bill == 20 and ((n10 > 0 and n5 > 0) or (n5 > 2)):
            n20 += 1
            if n10 > 0:
                n10 -= 1; n5 -= 1
            else:
                n5 -= 3
        else:
            break
    else:
        return True

    return False


bills = [5,5,5,10,20]

res = lemonadeChange(bills)

print(res)