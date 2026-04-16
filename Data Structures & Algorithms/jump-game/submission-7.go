
func canJump(nums []int) bool {
    n := len(nums)
    goal := n-1

    for i := goal-1; i>= 0; i-- {
        if nums[i] + i >= goal{
            goal = i
        }
    }
    return goal == 0


}
