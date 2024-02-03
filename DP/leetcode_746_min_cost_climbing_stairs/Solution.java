package DP.leetcode_746_min_cost_climbing_stairs;

class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int[] dp = new int[cost.length + 1];
        dp[0] = 0;
        dp[1] = 0;

        for (int i = 2; i < cost.length + 1; i++) {
            dp[i] = Math.min(dp[i-2] + cost[i-2], dp[i-1] + cost[i-1]);
        }
        
        return dp[cost.length];
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // Example usage
        int[] cost = {1, 100, 1, 1, 1, 100, 1, 1, 100, 1};
        int result = solution.minCostClimbingStairs(cost);
        System.out.println(result);
    }
}
