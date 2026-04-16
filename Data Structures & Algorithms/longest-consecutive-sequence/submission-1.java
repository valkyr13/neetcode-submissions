class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();
        HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();
        int len = nums.length;

        if(len == 0){
            return 0;
        }

        for(int i = 0; i<len;i++){
            set.add(nums[i]);
        }

        int curr;
        int currSequenceLength;
        int maxLen =  Integer.MIN_VALUE;

        for(int j=0; j<len;j++){
            if(!map.containsKey(nums[j]-1)){
                curr = nums[j];
                currSequenceLength = 0;
                while(set.contains(curr)){
                    currSequenceLength++;
                    curr--;
                }
                map.put(nums[j],currSequenceLength);
            }
            else{
                currSequenceLength = 1+map.get(nums[j]-1);
            }
            maxLen = Math.max(maxLen, currSequenceLength);
        }

        return maxLen;
    }
}
