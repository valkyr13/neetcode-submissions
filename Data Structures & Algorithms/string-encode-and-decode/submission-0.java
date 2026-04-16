class Solution {

    public String encode(List<String> strs) {
        List<String> list = new ArrayList<>();

        int len;
        char delimitor = '#';
        StringBuilder sb = new StringBuilder();


        for(String str: strs){
            len = str.length();
            sb.append(len);
            sb.append(delimitor);
            sb.append(str);
        }

        return sb.toString();

    }

    public List<String> decode(String str) {

        // 1. convert to character aarray
        // 2. use string functions

        int initialPosition = 0;
        int len;

        String subStr;

        int delimitorPosition;

        List<String> ans = new ArrayList<>();

        while(initialPosition < str.length()){
            delimitorPosition = initialPosition;

            while (str.charAt(delimitorPosition) != '#') delimitorPosition++;
            // delimitorPosition = str.indexOf('#', initialPosition);
            System.out.println(delimitorPosition);

            len = Integer.valueOf(str.substring(initialPosition,delimitorPosition));

            subStr = str.substring(delimitorPosition+1,delimitorPosition+len+1);

            ans.add(subStr);

            initialPosition = delimitorPosition+len+1;
        }

        return ans;

    }
}
