class Solution:
    def removeDuplicates(self, nums):
        '''
        type nums: List[int]
        rtype: int
        '''
        element = nums[0] # Storing the first element in a variable to use for duplicate analysis
        for n in nums[1:]: # Iterate over the array
            if n == element: nums.remove(n) # Verificate if actualy element is equal last. If positive, we remove this element
            else: element = n # Else, we modify value of the variable element
        return len(nums) # Finish, we return the array's lenght
    
'''
Best solution, by users of LeetCode:
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j
'''