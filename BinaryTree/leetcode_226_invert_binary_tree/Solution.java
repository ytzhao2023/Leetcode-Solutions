package BinaryTree.leetcode_226_invert_binary_tree;

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
    public TreeNode invertTree(TreeNode root) {
        traverse(root);
        return root;
    }

    void traverse(TreeNode root){
        if (root == null){
            return;
        }
        TreeNode temp = root.left;
        root.left = root.right;
        root.right = temp;

        traverse(root.left);
        traverse(root.right);   
    }
}
