class Solution {

    public void combinationSum(int[] nums, int target, int index, int sum, ArrayList<Integer> list, ArrayList<List<Integer>> ans) {
        System.out.println("list  : "+list);
        ArrayList<Integer> tempList = new ArrayList<>(list);
        sum += nums[index];
        tempList.add(nums[index]);
        System.out.println("list  : "+list);
        int diff = target - sum;
        // System.out.println("nums[index]: "+nums[index]);
        // System.out.println("sum: "+sum);
        // System.out.println("templist: "+tempList);

        System.out.println("diff: "+diff);

        if(diff< 0){
            System.out.println("templist: "+tempList);   
            return;
        } 

        if(diff == 0){
            System.out.println("sum: "+sum);
            // System.out.println("list: "+list);
            // System.out.println("ans: "+ans);
            ans.add(tempList);
            System.out.println("ans: "+ans);
            return;
        }

        System.out.println("list before appending : "+list);
        System.out.println("templist: "+tempList);


        for(int i = index; i<nums.length; i++){
            combinationSum(nums, target, i, sum, tempList, ans);
            System.out.println("list at this level: "+list);
        }

        return;

    }

    public List<List<Integer>> combinationSum(int[] nums, int target) {
        ArrayList<Integer> list = new ArrayList<>();
        ArrayList<List<Integer>> ans = new ArrayList<>();

        for(int i = 0; i<nums.length; i++){
            combinationSum(nums, target, i, 0, list, ans);
        }

        return ans;
    }
}
