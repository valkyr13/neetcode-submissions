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

    public boolean cmpTree(TreeNode root, TreeNode subRoot){
        if(root == null && subRoot == null){
            return true;
        }

        if(root != null && subRoot == null){
            return false;
        }

        if(root == null && subRoot != null){
            return false;
        }

        if(root.val == subRoot.val){
            return cmpTree(root.left, subRoot.left) && cmpTree(root.right, subRoot.right);
        }

        return false;


    }
    
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        if(root == null && subRoot == null){
            return true;
        }

        if(root != null && subRoot == null){
            return false;
        }

        if(root == null && subRoot != null){
            return false;
        }
        boolean subTree = false;
        if(root.val == subRoot.val){
            subTree = cmpTree(root, subRoot);
        }
        if(subTree == false){
            subTree = isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot) ;
        }

        return subTree;


    }
}
