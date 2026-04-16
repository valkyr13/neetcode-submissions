class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        //2 steps
        // find anagrams 

        // group anagrams without modfying og strings


        // hashmap sorted string -> actual string1, actual string2


        HashMap<String, List<String>> map = new HashMap<>();

        for (int i = 0; i< strs.length; i++){

            int[] charCount = new int[26];
            for(int j = 0; j< strs[i].length(); j++){
                charCount[strs[i].charAt(j) - 'a']++;
            }

            StringBuilder sb = new StringBuilder();
            for(int k = 0; k<26; k++){
                sb.append(charCount[k]);
                System.out.println(charCount[k]);
                sb.append("#");
            }

            System.out.println(sb.toString());

            if(!map.containsKey(sb.toString())){
                map.put(sb.toString(), new ArrayList<String>());
            }

            List<String> strList = map.get(sb.toString());

            strList.add(strs[i]);

        }

        return new ArrayList<>(map.values());
        
    }
}
