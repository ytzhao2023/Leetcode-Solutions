package DP.leetcode_70_climbing_stairs;

class Solution {
    public int climbStairs(int n) {
        if (n <= 1) {
            return 1;
        }

        int a = 1, b = 2;
        for (int i = 3; i < n+1; i ++) {
            int temp = a + b;
            a = b;
            b = temp;
            
        }
        return b;
        
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int result = solution.climbStairs(10);
        System.out.println(result);

    }
}

