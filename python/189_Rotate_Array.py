class Solution:# after viewing solution, because I don't wanna use extra space
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        # reverse all
        for ii in range(len(nums) // 2):
            temp = nums[ii]
            nums[ii] = nums[len(nums) - 1 - ii]
            nums[len(nums) - 1 - ii] = temp
        # reverse 0~k-1
        for ii in range(k // 2):
            temp = nums[ii]
            nums[ii] = nums[k - 1 - ii]
            nums[k - 1 - ii] = temp
        # reverse k~len-1
        for ii in range(k, (k + len(nums)) // 2):
            temp = nums[ii]
            nums[ii] = nums[len(nums) - 1 - (ii-k)]
            nums[len(nums) - 1 - (ii-k)] = temp