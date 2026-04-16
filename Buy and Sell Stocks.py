

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        return max_profit


if __name__ == "__main__":
    
    n = int(input("Enter number of days: "))
    prices = list(map(int, input("Enter prices separated by space: ").split()))
    
    
    if len(prices) != n:
        print("Error: Number of prices doesn't match days entered.")
    else:
        result = Solution().maxProfit(prices)
        print("Maximum Profit:", result)
