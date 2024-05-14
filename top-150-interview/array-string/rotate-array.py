from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # To solve this problem, it's necessary only take the last k elements and pull them to the start of the array
        k = k % len(nums)
        if k != 0:
            nums[:] = nums[len(nums)-k:] +  nums[:len(nums)-k]