class Solution {

    public int searchMinPos(int[] nums, int l, int r, int target){

        int mid = (l+r)/2;
        if(nums[mid] == target){
            return mid;
        }

        if(l>=r){
            return -1;
        }

        int num = searchMinPos(nums, l, mid, target);
        if(num == -1){
            return searchMinPos(nums, mid+1, r, target);
        }

        return num;

    }

    public int search(int[] nums, int target) {
        int l = 0;
        int min;
        int r = nums.length-1;

        int mid = (l+r)/2;
        
        int num = searchMinPos(nums, l, mid, target);
        if(num == -1){
            return searchMinPos(nums, mid+1, r,target);
        }

        return num;

    }
}
