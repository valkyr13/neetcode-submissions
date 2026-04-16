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
    public int kthSmallest(TreeNode root, int k) {
        //pq will not work because we need to set the k elements pnly
        //there's no way to keep track of size while recursively traversing the tree

        Stack<TreeNode> s = new Stack<TreeNode>();
        if(root == null || k == 0){
            return -1;
        }

        s.push(root);
        int ans = root.val;

        while(true){
            if(root.left != null){
                s.push(root.left);
                root = root.left;
                continue;
            }

            if(root.left == null){
                while(!s.isEmpty()){
                    TreeNode r = s.peek();
                    k--;
                    if(k == 0){
                        ans = r.val;
                        break;
                    }

                    s.pop();     

                    if(r.right != null){
                        s.push(r.right);
                        root = r.right;
                        break;
                    }
                }

                if(k == 0 && ans != -1){
                    break;
                }
            }
        }

        return ans;

    }
}

