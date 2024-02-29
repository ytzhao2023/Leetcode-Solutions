package BinaryTree.leetcode_654_maximum_binary_tree;

// Definition for a binary tree node.
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        return buildTree(nums, 0 , nums.length);   
    }

    private TreeNode buildTree(int[] nums, int start, int end) {
        if (start == end) return null;

        int maxIndex = maxIndex(nums, start, end);
        TreeNode root = new TreeNode(nums[maxIndex]);
        root.left = buildTree(nums, start, maxIndex);
        root.right = buildTree(nums, maxIndex + 1, end);

        return root;
    }

    private int maxIndex(int[] nums, int start, int end) {
        int maxIndex = start;
        for (int i = start; i < end; i++) {
            if (nums[i] > nums[maxIndex]) {
                maxIndex = i;
            }
        }
        return maxIndex;
    }
}