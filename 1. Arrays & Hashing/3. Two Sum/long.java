// Runtime 2ms
// Beats 98.89%

// Memory 45.06MB
// Beats 47.66%

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> remainingMap = new HashMap<>();
        for(int i = 0; i < nums.length; i++) {
            int remaining = target - nums[i];
            if(remainingMap.containsKey(remaining)) {
                return new int[]{remainingMap.get(remaining), i};
            }
            remainingMap.put(nums[i], i);
        }
        return new int[]{0, 0}; // Can return anything because every input has exactly one pair of indices
    }
}