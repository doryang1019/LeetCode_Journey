# Runtime 1ms
# Beats 99.86%

# Memory 56.17MB
# Beats 83.84%

public class Solution {
    public int MaxProfit(int[] prices) {
        int result = 0;
        int min = int.MaxValue;
        foreach(int price in prices) {
            if(price < min) {
                min = price;
            }
            if(price - min >= result) {
                result = price - min;
            }
        }
        return result;
    }
}