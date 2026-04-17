// Runtime 1ms
// Beats 99.02%

// Memory 49.25MB
// Beats 23.45%

public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> dict = new Dictionary<int, int>();
        for(int i = 0; i < nums.Length; i++) {
            int c = target - nums[i];
            if(dict.ContainsKey(c)) {
                return new int[] {dict[c], i};
            } else {
                dict[nums[i]] = i;
            }
        }
        return new int[] { };
    }
}