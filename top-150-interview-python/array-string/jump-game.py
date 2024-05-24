from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        maxPosition = 0
        for i in range(len(nums)-1):
            if i <= maxPosition:
                jump = nums[i] + i
                if jump > maxPosition:
                    maxPosition = jump
                if maxPosition >= len(nums)-1:
                    return True
        return False