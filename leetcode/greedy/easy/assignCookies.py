# Assigning Cookies to children

def assignCookies(children, cookies):
    cookies[:] = sorted(cookies, reverse=True)
    children[:] = sorted(children, reverse=True)
    cnt = 0; l1 = len(children) - 1; l2 =len(cookies) - 1
        
    i = j = 0

    while l1-i >= 0:
        while l2 - j >= 0:
            if children[l1-i] <= cookies[l2-j]:
                cnt += 1
                j += 1
                break
            j += 1
        i += 1
        
    return cnt