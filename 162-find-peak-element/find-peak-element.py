class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        n = len(nums)
        right = n - 1
        ans = 0

        while left <= right:
            curr = left + (right-left)//2

            if curr == 0 and curr < n-1 and nums[curr] > nums[curr+1]:
                ans = curr

            elif (curr == len(nums) - 1) and nums[curr] > nums[curr-1]:
                ans = curr

            elif curr > 0 and curr < n-1 and (nums[curr-1] < nums[curr] > nums[curr+1]):
                ans = curr

            if curr < n-1 and nums[curr] < nums[curr+1]:
                left = curr + 1
            
            else:
                right = curr - 1
            
        return ans

            