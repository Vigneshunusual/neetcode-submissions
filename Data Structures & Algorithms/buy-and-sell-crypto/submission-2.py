class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0
        minPrice=prices[0]
        n=len(prices)
        for i in range(1,n):
            if prices[i]<minPrice:
                minPrice=prices[i]
            else:
                profit=prices[i]-minPrice
                maxProfit=max(maxProfit,profit)
        return maxProfit
