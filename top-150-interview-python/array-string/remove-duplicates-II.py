from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, number, occurrences = 0, nums[0], 0 # Initialize variables to iterate over the array, store a number and the occurrences of this number
        while i < len(nums):
            if nums[i] == number: # When I iterate over the array, I look if the actually element is equal my last number. 
                occurrences += 1
                if occurrences > 2:
                    del nums[i]
                    continue
            else:
                number = nums[i]
                occurrences = 1
            i += 1
        return len(nums) # Finish, I return the lenght of the array