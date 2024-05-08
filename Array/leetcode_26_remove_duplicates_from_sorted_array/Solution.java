package List.leetcode_26_remove_duplicates_from_sorted_array;
class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0){
            return 0;  
        }
        int slow = 0;
        int fast = 1;
        while (fast < nums.length){
            if (nums[fast] != nums[slow]){
                slow ++;
                nums[slow] = nums[fast];
            }
            fast ++;
        }
        return slow + 1;
        
    }

   
}