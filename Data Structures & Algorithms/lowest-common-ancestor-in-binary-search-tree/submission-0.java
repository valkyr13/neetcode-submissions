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
public boolean presentInSubTree(TreeNode root, TreeNode child) {
        if(root == null){
            return false;
        }

        if(root.val == child.val){
            return true;
        }

        return presentInSubTree(root.left, child) || presentInSubTree(root.right, child);
        
    }
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(root == null){
            return null;
        }

        if(root.val == p.val || root.val == q.val){
            return root;
        }

        boolean left = false;
        boolean right = false;

        left = presentInSubTree(root.left, p);
        right =  presentInSubTree(root.right, q);

        if(left != true && right == true){
            return lowestCommonAncestor(root.right, p,q);
        } 

        if(left == true && right != true){
            return lowestCommonAncestor(root.left, p,q);
        }

        return root;

    }
}
