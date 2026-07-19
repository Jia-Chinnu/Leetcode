from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if not coins:
            return -1

        # DP array to store min coins for each amount
        s = [amount + 1] * (amount + 1)
        s[0] = 0  # 0 coins to make amount 0

        # Loop over each coin
        for coin in coins:
            for a in range(coin, amount + 1):
                s[a] = min(s[a], s[a - coin] + 1)

        return s[amount] if s[amount] <= amount else -1
