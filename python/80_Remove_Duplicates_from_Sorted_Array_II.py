class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 1
        count = 1
        last = nums[0]
        for fast in range(1, len(nums)):
            if nums[fast] == nums[fast - 1]:
                count += 1

            else:
                count = 1
            if count <= 2:
                # print(slow, fast)
                nums[slow] = nums[fast]
                slow += 1
        return slow


