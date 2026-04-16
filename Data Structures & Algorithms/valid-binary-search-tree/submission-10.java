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

    if(root.val >= max || root.val <= min){
        return false;
    }

    if(root.left != null){
        if(root.val > root.left.val){
            if(!isValid(root.left, min, root.val)){
                return false;
            }
        }else{
            return false;
        }
    }

    if(root.right != null){
        if(root.val < root.right.val){
            if(!isValid(root.right, root.val, max)){
                return false;
            }
        }else{
            return false;
        }
    }

    return true;

}
 public boolean isValidBST(TreeNode root) {
        if(root == null){
            return true;
        }

        int min = Integer.MIN_VALUE;
        int max = Integer.MAX_VALUE;

        return isValid(root, min, max);
    }
}