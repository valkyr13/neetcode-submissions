func trap(height []int) int {
	/*
	dp
	f(i) = min[max(0, i-1) , max(i+1,n-1)]
	two pointers
	start from 1 
	end at n-2
	keep track of max [n-1, i+1]
	*/
	n := len(height)
	left := make([]int, n)
	right := make([]int, n)

	
	left[0] = height[0]
	right[n-1] = height[n-1]
	trappedWater := 0

	for i := 1; i<n-1;i++{
		left[i] = max(left[i-1],height[i])
		right[n-i-1] = max(right[n-i],height[n-i-1])
	}
	for i := 1; i<n-1;i++{
		if  height[i] > min(left[i-1], right[i+1]){
			continue
		}
		trappedWater += min(left[i-1], right[i+1]) - height[i]
	}
	return trappedWater


}
