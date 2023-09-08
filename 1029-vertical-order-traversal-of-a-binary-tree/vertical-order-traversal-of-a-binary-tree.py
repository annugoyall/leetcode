# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [[root, 0]]
        dict = {}
        ans = []
        while queue:
            curr = queue
            queue = []

            for node, ind in curr:
                if ind in dict:
                    dict[ind].append(node.val)
                else:
                    dict[ind] = [node.val]

                
                if node.left:
                    queue.append([node.left, ind-1])

                if node.right:
                    queue.append([node.right, ind+1])

            queue.sort(key = lambda x: x[0].val)
        
        for i in sorted(dict):
            ans.append(dict[i])

        return ans


