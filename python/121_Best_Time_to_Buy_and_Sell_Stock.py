# class Solution: # brute force time exceed
#     def maxProfit(self, prices: List[int]) -> int:
#         profit = 0
#         for buy in range(len(prices) - 1):
#             for sell in range(buy + 1, len(prices)):
#                 profit = max(profit, prices[sell] - prices[buy])
#         return profit

class Solution:# similar to https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/submissions/566840001/
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        profit = 0
        inside_hand = [0 for ii in range(len(prices) - 1)]
        inside_hand[0] = -prices[0]
        for ii in range(1, len(prices) - 1):
            inside_hand[ii] = max(inside_hand[ii - 1], -prices[ii])

        outside_hand = [0 for _ in range(len(prices))]
        for ii in range(1, len(prices)):
            outside_hand[ii] = max(outside_hand[ii - 1], inside_hand[ii - 1] + prices[ii])
            profit = max(profit, outside_hand[ii]) # this max may be redundant(after viewing solution)
        return profit

# official solution:
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         inf = int(1e9)
#         minprice = inf
#         maxprofit = 0
#         for price in prices:
#             maxprofit = max(price - minprice, maxprofit)
#             minprice = min(price, minprice)
#         return maxprofit
