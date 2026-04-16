class Solution {

    public int getMaxFreq(HashMap<Character,Integer> map){
        int max = Integer.MIN_VALUE;
        for(Character ch: map.keySet()){
            max = Math.max(map.get(ch), max);
        }

        return max;
    }


    public int characterReplacement(String s, int k) {
        
        HashMap<Character,Integer> map = new HashMap<>();

        int l = 0;
        int r = 0;
        int len;
        int lVal;
        int rVal;
        int maxLen = Integer.MIN_VALUE;

        while(l <=r && r < s.length()){
            rVal = 0;
            if(map.containsKey(s.charAt(r))){
                rVal = map.get(s.charAt(r));
            }
            map.put(s.charAt(r), rVal+1);

            len = r-l+1;
            if(len - getMaxFreq(map) <= k){
                maxLen = Math.max(maxLen, len);
            }else{
                lVal = map.get(s.charAt(l));
                map.put(s.charAt(l), lVal-1);
                l++;
            }
            r++;
            

        }

        return maxLen;
    }
}
