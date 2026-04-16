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
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        int mid = 0;
        int len = inorder.length;
        if (len == 0){
            return null;
        }
        TreeNode root = new TreeNode(preorder[0]);

        for(int i = 0;i<len;i++){
            if(inorder[i] == preorder[0]){
                mid = i;
                break;
            }
        }

//Copy range=> for elements from i to j-> give indices as i, j+1
        int[] leftInorder = Arrays.copyOfRange(inorder, 0, mid);
        int[] rightInorder = Arrays.copyOfRange(inorder, mid+1, len);
        int[] leftPreorder = Arrays.copyOfRange(preorder, 1, mid+1);
        int[] rightPreorder = Arrays.copyOfRange(preorder, mid+1, len);

        root.left = buildTree(leftPreorder, leftInorder);
        root.right = buildTree(rightPreorder, rightInorder);
 
        return root;
    }
}
