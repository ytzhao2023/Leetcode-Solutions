package List.leetcode_977_squares_of_a_sorted_array;

public class Solution {
    public int[] sortedSquares(int[] nums) {
        int left = 0;
        int right = nums.length - 1;
        int[] result = new int[nums.length];
        int resultIndex = nums.length - 1;

        while (left <= right){

            if (nums[left] * nums[left] > nums[right] * nums[right]){
                result[resultIndex] = nums[left] * nums[left];
                left ++;
                resultIndex --;
            }else{
                result[resultIndex] = nums[right] * nums[right];
                right --;
                resultIndex --;
            }
        }
        return result;
    }   
}

