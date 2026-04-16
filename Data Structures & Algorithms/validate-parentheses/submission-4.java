class Solution {

    public boolean openingBracket(Character ch){
        switch(ch){
            case '[': return true;
            case '{': return true;
            case '(': return true;
            default: return false;
        }
    }

        
    public boolean closingBracket(Character ch){
        switch(ch){
            case ']': return true;
            case '}': return true;
            case ')': return true;
            default: return false;
        }
    }



    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>(); 

        int len = s.length();
        if(len == 0) return true;

        for(int i = 0;i<len;i++){
            Character ch = s.charAt(i);

            if (closingBracket(ch) && !stack.isEmpty()){
                Character top =  stack.peek();
                if((ch == ']' && top == '[') || (ch == ')' && top == '(') ||  (ch == '}' && top == '{')){
                    stack.pop();
                }
                else{
                    return false;
                }
            }
            else if (closingBracket(ch) && stack.isEmpty()){
                return false;
            }
            else if (openingBracket(ch)){
                stack.push(ch);
            }
        }

        if(!stack.isEmpty()){
            return false;
        }

        return true;

         
        
    }
}
