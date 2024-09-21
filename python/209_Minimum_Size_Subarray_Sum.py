# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         if sum(nums) < target:
#             return 0
#         lo = 0
#         hi = 0
#         min_len = len(nums)
#         sum1 = 0
#         while lo < len(nums) or hi < len(nums):
            
#             if sum1 >= target:
#                 min_len = min(min_len, hi - lo)
#                 sum1 -= nums[lo]
#                 lo += 1
#             elif hi < len(nums):
#                 sum1 += nums[hi]
#                 hi += 1
#             else:
#                 lo += 1
#             # print(lo, hi, sum1, min_len)
#             # if hi == len(nums) and lo >= hi - min_len:
#             #     break
#         return min_len

# after viewing solution: remove sum()
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        lo, hi = 0, 0
        min_len = len(nums) + 1
        sum1 = 0
        while lo < len(nums) or hi < len(nums):
            
            if sum1 >= target:
                min_len = min(min_len, hi - lo)
                sum1 -= nums[lo]
                lo += 1
            elif hi < len(nums):
                sum1 += nums[hi]
                hi += 1
            else:
                lo += 1
        return min_len if min_len != len(nums) + 1 else 0
