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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> ans = new ArrayList<>();

        Queue<TreeNode> queue = new LinkedList<>();

        if(root == null){
            return ans;
        }

        queue.add(root);
        ans.add(new ArrayList<>(Arrays.asList(root.val)));
        int len;

        while(!queue.isEmpty()){
            len = queue.size();
            List<Integer> currLevel = new ArrayList<>();


            while(len>0){
                TreeNode currNode = queue.remove();
                len--;

                if(currNode.left != null){
                    queue.add(currNode.left);
                    currLevel.add(currNode.left.val);
                }
                if(currNode.right != null){
                    queue.add(currNode.right);
                    currLevel.add(currNode.right.val);
                }

            }

            if(currLevel.size()>0){
                ans.add(currLevel);
            }
        }


        return ans;
    }
}
