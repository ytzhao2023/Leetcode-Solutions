package List.leetcode_283_move_zeroes;

import java.util.Arrays;

class OneMethd {
    public void moveZeroes(int[] nums) {

        int l = 0, r = 0;
        while (r < nums.length) {
            if (nums[r] != 0) {
                int temp;
                temp = nums[l];
                nums[l] = nums[r];
                nums[r] = temp;
                l++;
            }
            r++;
        }   
    }
}

class Solution {
    public static void main(String[] args) {
        OneMethd method = new OneMethd();

        int [] myList = {1, 2, 3, 4, 7, 0, 0, 10};

        method.moveZeroes(myList);

        System.out.println(Arrays.toString(myList));
        
    }

}





