package BinaryTree.leetcode_114_flatten_binary_tree_to_linked_list;

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
    public void flatten(TreeNode root) {
        if (root == null) return;

        // 将二叉树的左孩子和右孩子都展开成链表
        flatten(root.left);
        flatten(root.right);   
        
        // 将左孩子存储在left中，将右孩子存储在right中
        TreeNode left = root.left;
        TreeNode right = root.right;

        // 让左孩子设置为null，从二叉树中剥离出来，之后让根节点的右侧指向左孩子
        root.left = null;
        root.right = left;

        // 将root赋值给p，遍历p，找到最末尾的p点
        TreeNode p = root;
        while (p.right != null){
            p = p.right;
        }

        // 让p.right指向原来右孩子保存的right，把链表连接起来
        p.right = right;
    }
}