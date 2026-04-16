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

public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        if(root == null){
            return "#";
        }

        return root.val + "," + serialize(root.left) + ","+serialize(root.right);
    }


    public TreeNode deserializeHelper(Queue<String>  q){

        String top = q.poll();
        if(top.equals("#")){
            return null;
        }

        TreeNode root = new TreeNode(Integer.parseInt(top));

        root.left =  deserializeHelper(q);
        root.right = deserializeHelper(q);

        return root;


    }



    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if (data == ""){
            return null;
        }

        Queue<String> q = new LinkedList<>(Arrays.asList(data.split(",")));
        //in java int array or any string or object is pased by refrence -> i can use it to persist values across all call stacks!!
// arrays and string s are treated as onjects in java
        return deserializeHelper(q);
    }
}
