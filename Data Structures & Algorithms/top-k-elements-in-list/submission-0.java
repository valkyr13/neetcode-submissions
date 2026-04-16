class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int maxFreq = nums.length;
        int freq;

        List<Integer>[] freqTable = new ArrayList[nums.length + 1];

        HashMap<Integer,Integer> map = new HashMap<>();

        for (int i = 0; i< nums.length;i++){
            System.out.println(nums[i]);

            if(map.containsKey(nums[i])){
                freq = map.get(nums[i]);
                map.put(nums[i], freq+1);

            }else{
                map.put(nums[i], 1);
            }
            System.out.println(nums[i]+ ":" + map.get(nums[i]));

        }

        for (int key : map.keySet()){
            freq = map.get(key);
            System.out.println(key+": "+ freq);

            if(freqTable[freq] == null){
                freqTable[freq] = new ArrayList<>();
            }
            
            freqTable[freq].add(key);
        }

        System.out.println(Arrays.toString(freqTable));

        int[] res = new int[k];
        int idx = 0;

        for (int j = nums.length;j>0;j--){
            if(freqTable[j] != null){
                for(int val : freqTable[j]){
                    if(idx < k ){
                    res[idx] = val;
                    idx++;
                   }else{
                        break;
                   }   
                }
            }
        }

        return res;
        
        
    }
}
