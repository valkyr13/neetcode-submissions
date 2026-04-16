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
    public int maxDepth(TreeNode root, int currDepth) {
        currDepth++;

        int left = currDepth;
        int right = currDepth;

        if(root.left != null){
            left = maxDepth(root.left,currDepth);
        }

        if(root.right != null){
            right = maxDepth(root.right,currDepth);
        }

        return right - left >= 0 ? right: left;


    }
    
    public int maxDepth(TreeNode root) {
        if(root == null){
            return 0;
        }

        int currDepth = 1;
        int left = currDepth;
        int right = currDepth;

        if(root.left != null){
            left = maxDepth(root.left,currDepth);
        }

        if(root.right != null){
            right = maxDepth(root.right,currDepth);
        }

        return right - left >= 0 ? right: left;
        
        
    }
}
