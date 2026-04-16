// Runtime 7ms
// Beats 98.46%

// Memory 73.70MB
// Beats 42.68%

public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        Dictionary<int, int> dict = new Dictionary<int, int>();
        foreach (int num in nums) {
            if(!dict.ContainsKey(num)) {
                dict.Add(num, 1);
            } else {
                return true;
            }
        }

        return false;
    }
}