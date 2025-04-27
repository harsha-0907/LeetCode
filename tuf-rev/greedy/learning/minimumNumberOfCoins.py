class Solution:
    def minPartition(self, N):
        coins = sorted([1, 2, 5, 10, 20, 50, 100, 200, 500, 2000], reverse=True)
        coins_taken = []; pos  = 0
        while N > 0:
            number_of_coins = N // coins[pos]
            if number_of_coins > 0:
                coins_taken.extend([coins[pos]] * number_of_coins)
                N -= (number_of_coins * coins[pos])
            pos += 1
        return coins_taken