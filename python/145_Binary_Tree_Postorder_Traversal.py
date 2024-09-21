# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        stack = [[None, None]]
        cur = root
        state = 0
        while len(stack) and state is not None:
            if not cur:
                cur, state = stack.pop()
                continue
            if state == 0:
                stack.append([cur, 1])
                cur = cur.left
                state = 0
            elif state == 1:
                stack.append([cur, 2])
                cur = cur.right
                state = 0
            else:
                output.append(cur.val)
                cur, state = stack.pop()
        return output