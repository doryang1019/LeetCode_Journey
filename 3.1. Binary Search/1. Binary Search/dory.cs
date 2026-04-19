// Runtime 0ms
// Beats 100.00%

// Memory 53.02MB
// Beats 13.64%

public class Solution {
    public int Search(int[] nums, int target) {
        int left = 0;
        int right = nums.Length - 1;
        int result = -1;
        if(nums.Length == 1 && nums[0] == target) {
            return 0;
        }
        while(left < right) {
            if(nums[left] == target) {
                return left;
            }
            if(nums[right] == target) {
                return right;
            }
            int medium = (right + left) / 2;
            if(nums[medium] == target) {
                return medium;
            } else if (nums[medium] < target) {
                left = medium + 1;
            } else {
                right = medium - 1;
            }
        }
        return result;
    }
}