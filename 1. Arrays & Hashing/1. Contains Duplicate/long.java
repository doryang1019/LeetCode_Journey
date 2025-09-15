// Runtime 19ms
// Beats 37.35%

// Memory 59.93MB
// Beats 19.64%

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> numsSet = new HashSet<>();
        for(int num : nums) {
            numsSet.add(num);
        }
        return numsSet.size() != nums.length;
    }
}