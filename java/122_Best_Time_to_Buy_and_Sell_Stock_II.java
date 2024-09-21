class Solution {
    public int maxProfit(int[] prices) {
// profit = prices[sell] - prices[buy]
// sell > buy >= 0 or sell == buy == -1
        int[] outside_hand = new int[prices.length];
        int[] inside_hand = new int[prices.length];
        inside_hand[0] = -prices[0];
        outside_hand[0] = 0;
        int profit = 0;

        for (int ii = 1; ii < prices.length; ++ii) {
            inside_hand[ii] = Math.max(inside_hand[ii - 1], outside_hand[ii - 1] - prices[ii]);
            outside_hand[ii] = Math.max(outside_hand[ii - 1], inside_hand[ii - 1] + prices[ii]);
            profit = Math.max(profit, outside_hand[ii]);
            // System.out.printf("%d,%d,%d,%d\n", ii, inside_hand[ii], outside_hand[ii], profit);
        }
        return profit;
    }
}