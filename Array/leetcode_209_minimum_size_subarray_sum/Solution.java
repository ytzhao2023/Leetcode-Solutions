package List.leetcode_209_minimum_size_subarray_sum;

public class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int left = 0;
        int sumSubarray = 0;
        int minLength = Integer.MAX_VALUE;
        for (int right = 0; right < nums.length; right++){
            sumSubarray += nums[right];
            while (sumSubarray >= target){
                minLength = Math.min(minLength, right - left + 1);
                sumSubarray -= nums[left];
                left += 1;
            }
        }
        return minLength == Integer.MAX_VALUE ? 0 : minLength;
    }
    
}
