# Coin Change

def coinChangeGreedy(coins, total):
    coins[:] = sorted(coins, reverse=True)
    number_of_coins = 0

    for coin in coins:
        number_of_coins += total // coin
        total = total % coin
    
    if total > 0:
        return -1
    
    return number_of_coins

def coinChangeDP(coins, total):
    """To solve the coin change question using dp"""
    dp = dict(); MAX_SIZE = 9999999
    def coinChange(total, pos, number):
        if total == 0:
            return number
        if pos == len(coins):
            return MAX_SIZE
        
        if (total, pos) in dp:
            return dp[(total, pos)]
        
        if total < coins[pos]:
            dp[(total, pos)] = coinChange(total, pos + 1, number)
        else:
            take_coin = coinChange(total - coins[pos], pos, number + 1)
            skip_coin = coinChange(total, pos + 1, number)
            dp[(total, pos)] = min(take_coin, skip_coin)
        
        return dp[(total, pos)]
    
    result = coinChange(total, 0, 0)
    
    return result if result < MAX_SIZE else -1

coins = [9, 6, 5, 1]
total = 11

res = coinChangeDP(coins, total)

print(res)