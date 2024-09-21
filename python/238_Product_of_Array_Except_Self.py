# after viewing solution
class Solution:
    def leftProduct(self, nums, n):
        if self.lp[n] is not None:
            return self.lp[n]
        if n == 0:
            self.lp[n] = 1
        else:
            self.lp[n] = self.leftProduct(nums, n - 1) * nums[n - 1]
        return self.lp[n]
    def rightProduct(self, nums, n):
        if self.rp[n] is not None:
            return self.rp[n]
        if n == len(nums) - 1:
            self.rp[n] = 1
        else:
            self.rp[n] = self.rightProduct(nums, n + 1) * nums[n + 1]
        return self.rp[n]
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        self.lp = [None for _ in nums]
        self.rp = [None for _ in nums]
        for ii in range(len(nums)):
            result.append(self.leftProduct(nums, ii) * self.rightProduct(nums, ii))
        # print(self.lp, self.rp)
        return result

# # high rate comments: double ptr
# std::vector<int> productExceptSelf2(std::vector<int>& nums) {
#     std::vector<int> answer(nums.size(), 1);
#     int left = 0, right = nums.size() - 1;
#     int lp = 1, rp = 1;
#     while (right >= 0 && left < nums.size()) {
#         answer[right] *= rp;
#         answer[left] *= lp;
#         lp *= nums[left++];
#         rp *= nums[right--];
#     }
#     return answer;
# }