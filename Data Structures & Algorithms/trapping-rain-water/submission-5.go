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
	
	left := 1
	right := n-2
	leftMax := height[0]
	rightMax := height[n-1]
	trappedWater := 0
	// O(n) time and O(1) SPACE

	for left <= right {
		if leftMax < rightMax{
			if height[left] < leftMax{
				trappedWater += leftMax - height[left]
			}
			leftMax = max(leftMax, height[left])
			left++
		}else{
			if height[right] < rightMax{
				trappedWater += rightMax - height[right]
			}
			rightMax = max(rightMax, height[right])
			right--
		}

	}

	return trappedWater
}
