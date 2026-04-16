/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public void invertNode(TreeNode root) {



        TreeNode temp = root.left;
        root.left = root.right;
        root.right = temp;

        if(root.left != null){
            invertNode(root.left);
        }
        if(root.right != null){
            invertNode(root.right);
        }

        return;  
    }

    public TreeNode invertTree(TreeNode root) {

        if(root == null){
            return root;
        }
        TreeNode temp;

        temp = root.left;
        root.left = root.right;
        root.right = temp;

        if(root.left != null){
            invertNode(root.left);
        }
        if(root.right != null){
            invertNode(root.right);
        }

        return root;


        
    }
}
