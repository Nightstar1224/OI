# state represents line number or rsp register
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        cur = root
        stack = [[root, 0]]
        state = 0
        while len(stack):
            if not cur:
                cur, state = stack.pop()
                continue
            if state == 0:
                stack.append([cur, 1])
                cur = cur.left
                state = 0
            elif state == 1:
                output.append(cur.val)
                stack.append([cur, 2])
                cur = cur.right
                state = 0
            else:
                cur, state = stack.pop()
        return output
