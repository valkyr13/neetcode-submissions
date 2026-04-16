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
 
public boolean isValid(TreeNode root, int min, int max){

    if(root == null){
        return true;
    }

    if(root.val >= max || root.val <= min){
        return false;
    }

    return isValid(root.left, min, root.val) && isValid(root.right, root.val, max);

}
 public boolean isValidBST(TreeNode root) {
        if(root == null){
            return true;
        }

        int min = Integer.MIN_VALUE;
        int max = Integer.MAX_VALUE;

        return isValid(root.left, min, root.val) && isValid(root.right, root.val, max);
    }
}
