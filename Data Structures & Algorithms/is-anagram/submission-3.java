class Solution {
    public boolean isAnagram(String s, String t) {
        // sort it

        // o(nlogn)*2 + o(n) {compare}

        // hash map increase, decrease

        // o(n) memory, o(n)*3 time

        if (s.length() != t.length()){
            return false;
        }

        

        HashMap<Character, Integer> map = new HashMap<>();
        int freq;

        for(int i = 0; i<s.length(); i++){
            freq = 1;
            if(map.containsKey(s.charAt(i))){
                freq = map.get(s.charAt(i));
                freq += 1;
            }

            map.put(s.charAt(i), freq);
        }

        for(int j = 0; j<t.length(); j++){
            if(map.containsKey(t.charAt(j))){
                freq = map.get(t.charAt(j));
                freq -= 1;
                map.put(t.charAt(j),freq);
            }
            else{
                return false;
            }
        }

     for (Map.Entry<Character, Integer> entry : map.entrySet()) {
            if(entry.getValue() != 0){
                return false;
            }
    }

    return true;



    }
}
