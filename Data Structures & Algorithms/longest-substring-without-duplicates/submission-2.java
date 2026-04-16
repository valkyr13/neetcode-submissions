class Solution {
    public int lengthOfLongestSubstring(String s) {
        int maxLen = Integer.MIN_VALUE;

        int l = 0;
        int r = 1;

        int len = s.length();
        if(len == 0){
            return 0;
        }
        if(len == 1){
            return 1;
        }

        Character ch;

        HashSet<Character> set = new HashSet<>();

        set.add(s.charAt(l));

        while(r < len){
            ch = s.charAt(r);
            while(set.contains(ch)){
                set.remove(s.charAt(l));
                l++;
            }
            set.add(s.charAt(r));
            r++;
            maxLen = Math.max(maxLen, r-l);
        }

        return maxLen;   
    }
}
