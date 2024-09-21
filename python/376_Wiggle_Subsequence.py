class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # turn = 1
        # ii = 1
        # length_valley = [1 for _ in nums] # max length before equal ii + 1
        # length_peak = [1 for _ in nums]
        # while ii < len(nums) - 1:
        #     if nums[ii - 1] < nums[ii] and nums[ii] > nums[ii + 1]:
        #         length_peak[ii] = length_valley[ii - 1] + 1
        #         length_valley[ii] = length_valley[ii - 1]
        #     elif nums[ii - 1] > nums[ii] and nums[ii] < nums[ii + 1]:
        #         length_valley[ii] = length_peak[ii - 1] + 1
        #         length_peak[ii] = length_peak[ii - 1]
        #     else:
        #         length_peak[ii] = length_peak[ii - 1]
        #         length_valley[ii] = length_valley[ii - 1]
        direction = -1
        length = 1
        for ii in range(1, len(nums)):
            if direction == -1:
                if nums[ii] != nums[ii - 1]:
                    length += 1
                    direction = int(nums[ii - 1] < nums[ii])
            elif direction == 1:#inc
                if nums[ii - 1] > nums[ii]:
                    length += 1
                    direction = 0
            else:#direction == 0 dec
                if nums[ii - 1] < nums[ii]:
                    length += 1
                    direction = 1
            # print(direction, length, nums[ii - 1], nums[ii])
        return length

        