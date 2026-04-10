class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuyRate=prices[0]
        maxprofit=0
        profit=0

        for i in range(1,len(prices)):
            if prices[i]>minBuyRate:
                profit=prices[i]-minBuyRate
                maxprofit=max(maxprofit,profit)
            else:
                minBuyRate=prices[i]

        return maxprofit
