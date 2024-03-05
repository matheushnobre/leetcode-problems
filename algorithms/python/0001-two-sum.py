class Solution:
    def twoSum(self, nums, target):
        '''
        type nums: List[int]
        type target: int
        rtype: List[int]
        '''
        map = {}
        for index, i in enumerate(nums):
            if target - i in map:
                return map[target-i], index
            else:
                map[i] = index