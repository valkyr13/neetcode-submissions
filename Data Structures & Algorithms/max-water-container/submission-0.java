class Solution {
    public int maxArea(int[] heights) {
        int len = heights.length;
        int l = 0;
        int r = len-1;
        int maxWater = Integer.MIN_VALUE;
        int h;
        int diff;


        while(l<r){

            h = Math.min(heights[l], heights[r]);
            diff = r-l;
            maxWater = Math.max(maxWater, h*diff);

            if (heights[l]<= heights[r]){
                l++;
            }

            else{
                r--;
            }
        }

    return maxWater;
        
    }
}
