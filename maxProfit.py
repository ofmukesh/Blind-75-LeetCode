class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=prices[0];
        profit=0;

        for curr_price in prices:
            min_price=min(min_price,curr_price);
            profit=max(profit,curr_price-min_price);

        return profit;
