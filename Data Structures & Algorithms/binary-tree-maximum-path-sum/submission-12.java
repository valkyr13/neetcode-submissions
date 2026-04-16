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
    public int[] maximisePathSum(TreeNode root){
        int[] ans = new int[2];
        // int leftPath = 0;
        // int rightPath = 0;
        int[] leftAns = new int[2];
        int[] rightAns = new int[2];


        if(root.left == null && root.right == null){
            ans[0] = root.val;
            ans[1] = root.val;
        System.out.println("root: "+root.val+", maxAns at Root level: "+ans[1]+", "+ans[0]);
            return ans;
        }

        if(root.left != null){
            leftAns = maximisePathSum(root.left);
            // leftPath = Math.max(leftAns[0], 0);
        }

        if(root.right != null){
            rightAns = maximisePathSum(root.right);
            // rightPath = Math.max(rightAns[0], 0);
        }

        ans[0] = Math.max(root.val, Math.max(root.val+leftAns[0], root.val+rightAns[0]));
    System.out.println("root: "+root.val+", left ans: "+leftAns[0]+", left ans_1: "+leftAns[1]);
System.out.println("root: "+root.val+", right ans: "+rightAns[0]+", right ans_1: "+rightAns[1]);

        if(root.right == null){
            // I need to diffentiate between having no Child and having a child with sum zero
            ans[1] = Math.max(leftAns[1],Math.max(root.val,root.val+leftAns[0]));
            return ans;
        }

        if(root.left == null){
            ans[1] = Math.max(rightAns[1],Math.max(root.val,root.val+rightAns[0]));
            return ans;
        }

        ans[1] = Math.max(Math.max(leftAns[1], rightAns[1]),Math.max(ans[0],(root.val+leftAns[0]+rightAns[0])));
        System.out.println("root: "+root.val+", maxAns at Root level: "+ans[0]+", "+ans[1]);
        return ans; 
    }

    public int maxPathSum(TreeNode root) {
        return maximisePathSum(root)[1];
    }
}