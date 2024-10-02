# class Stack(list):
#     def append(self, a):
#         print('append', a)
#         super().append(a)
#     def pop(self):
#         print('pop')
#         return super().pop()
class Solution:
    def trap(self, height: List[int]) -> int:
        # very hard to handle the boundary
        # # double pointers
        # # lo = 0
        # # hi = len(height) - 1
        # # area = 0
        # # last_layer = 0
        # # while lo < hi:
        # #     if height[lo] <= last_layer:
        # #         lo += 1
        # #         continue
        # #     if height[hi] <= last_layer:
        # #         hi -= 1
        # #         continue
        # #     if height[lo] < height[hi]:
        # #         area += (hi - lo + 1) * (height[lo] - last_layer)
        # #         last_layer = height[lo]
        # #         lo += 1
        # #     else:
        # #         area += (hi - lo + 1) * (height[hi] - last_layer)
        # #         last_layer = height[hi]
        # #         hi -= 1
        # #     print(lo, hi, area, last_layer)
        # # return area - sum(height)
        # lo = 0
        # hi = len(height) - 1
        # last_layer = 0
        # area = 0
        # while True:
        #     while height[lo] <= last_layer and lo < hi:
        #         lo += 1
        #     while height[hi] <= last_layer and lo < hi:
        #         hi -= 1
        #     if height[lo] < height[hi]:
        #         area += (height[lo] - last_layer) * (hi - lo + 1)
        #         last_layer = height[lo]
        #     else:
        #         area += (height[hi] - last_layer) * (hi - lo + 1)
        #         last_layer = height[hi]
        #     # print(lo, hi, area, last_layer)
        #     if lo >= hi:
        #         break
        # return area - sum(height)
        stack = []
        water = 0
        ii = 0
        while ii < len(height):
            if 0 == len(stack) or height[ii] < height[stack[-1]]:
                stack.append(ii)
                ii += 1
            else:
                while len(stack) and height[ii] >= height[stack[-1]]:
                    top = stack.pop()
                    if len(stack) == 0:
                        break
                    cur_height = min(height[ii], height[stack[-1]]) - height[top]
                    water += (ii - stack[-1] - 1) * cur_height
                # stack.append(ii)
            # print(ii, stack, water)
        return water
                    

sl = Solution()
sl.trap([4,2,0,3,2,5])