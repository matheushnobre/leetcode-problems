from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, lenght = 0, len(nums) # Initialize two variables: one to iterate over the array and other to store the array's lenght
        while i < lenght:
            if nums[i] == val: # If i find a occurrence of the value in the array, I remove this occurrence and i decrease the variable lenght. I don't need to increment variable i in this case 
                del nums[i]
                lenght -= 1
            else: # Else, I increment i
                i += 1
        return lenght # Finish, I return the lenght of the array