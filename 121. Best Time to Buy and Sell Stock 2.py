from typing import List


def maxProfit2(prices: List[int]) -> int:
    profit = 0
    for i in range(1, len(prices)):
        profit += max(prices[i] - prices[i - 1], 0)
    return profit

maxProfit2([7,1,5,3,6,4])