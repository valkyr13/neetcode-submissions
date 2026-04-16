
func helper(i int,nums []int, dp []bool) bool{
    if i == 0 {
        dp[i] = true
        return true
    }

    if dp[i] == true{
        return true
    }

    for j := i-1; j>= 0;j-- {
        if nums[j] + j >= i && helper(j,nums, dp) == true {
            dp[i] = true
             break
        }
    }
    return dp[i]
}

func canJump(nums []int) bool {
    n := len(nums)

    dp := make([]bool,n)

    helper(n-1,nums,dp)

    return dp[n-1]

    

}
