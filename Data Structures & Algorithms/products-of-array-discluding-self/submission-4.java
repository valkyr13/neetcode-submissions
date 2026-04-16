class Solution {
    public int[] productExceptSelf(int[] nums) {
        HashMap<Integer, Integer> rightProductMap = new HashMap<>();
        HashMap<Integer, Integer> leftProductMap = new HashMap<>();

        int l = 1;
        int len = nums.length;
        int r = len-2;

        int rightProduct = 1;
        int leftProduct = 1;

        //beware of duplicate nums in array!

        while(r > -1){
            rightProduct *= nums[r+1];
            rightProductMap.put(r, rightProduct);
            System.out.println("rightProduct at "+  "for: "+ r);
            System.out.println(rightProduct);
            r--;
        }


        while(l < len){
            leftProduct *= nums[l-1];
            leftProductMap.put(l, leftProduct);
            System.out.println("leftProduct at "+" for: "+ l);
            System.out.println(leftProduct);
            l++;
        }

        int j = 0;

        int[] productSelf = new int[len];
        int product;
        while(j < len){
            product = 1;
            if(rightProductMap.containsKey(j)){
                product *= rightProductMap.get(j);
                System.out.println("rightProductMap at "+ j);
                System.out.println(rightProductMap.get(j));
            }

            if(leftProductMap.containsKey(j)){
                product *= leftProductMap.get(j);
                System.out.println("leftProductMap at "+ j);
                System.out.println(leftProductMap.get(j));
            }
            productSelf[j] = product;
            j++;
        }


        return productSelf;
    }
}  
