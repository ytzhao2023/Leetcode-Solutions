// package DP.leetcode_494_target_sum;

// class Solution {
//     public int findTargetSumWays(int[] nums, int target) {
//         int sum = 0;
//         for(int i = 0; i < nums.length; i++){
//             sum += nums[i];
//         }

//         if ((target + sum)%2 != 0){
//             return 0; 
//         }
    

//         if (Math.abs(target) > sum){
//             return 0;
//         }

//         int positive = (sum + target) / 2;
//         int[][] dp = new int[nums.length][positive + 1];  

        
//     }
// }
