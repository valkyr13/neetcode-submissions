class Solution {
    public int findMin(int[] nums, int l, int r){

        if(l>=r){
            return nums[r];
        }

        int min;
        int mid = (l+r)/2;

        return min = Math.min(findMin(nums, l, mid),findMin(nums, mid+1, r));
    }
    public int findMin(int[] nums) {

        int l = 0;
        int min;
        int r = nums.length-1;

        int mid = (l+r)/2;

        return min = Math.min(findMin(nums, l, mid),findMin(nums, mid+1, r));
        
    }
}
