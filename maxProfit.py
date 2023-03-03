class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price=prices[0];
        max_profit=0;

        for price in prices:
            buy_price=min(buy_price,price);
            max_profit=max(max_profit,price-buy_price);
            
        return profit;

    
# Psuedocode
# Intialize two variables that contain buy price and max profit
# check stock price - each day -> 
#     store current price in buy_price if current price < previous buy price 
#     else store profit in max_profit if profitable then max_profit
# return max_profit

