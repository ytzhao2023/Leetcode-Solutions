package List.leetcode_27_remove_element;

class Solution {
    public int removeElement(int[] nums, int val) {
        int slowIndex = 0;
        for (int i = 0; i < nums.length; i++ ){
            if (nums[i] != val){
                nums[slowIndex] = nums[i];
                slowIndex ++;
            }
        }
        return slowIndex;
    }
}
