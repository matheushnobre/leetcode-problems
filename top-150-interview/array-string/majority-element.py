from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        elements = set(nums) # I used this because it's more eficient to count the occurrences of an element in array next. Without set, I received time limit exceeded
        for e in elements:
            if nums.count(e) > n / 2:
                return e