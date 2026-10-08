class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        n = len(prices)
        maxi = 0
        mini = prices[0]

        for i in range(n):
            profit = prices[i] - mini
            maxi = max(maxi, profit)
            mini = min(mini, prices[i])
        
        return maxi