from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        del nums1[m:] # Deleting 0 at end of the array (I prefer)
        nums1.extend(nums2) # Exteding array 2 in array 1
        nums1.sort() # Sorting array using the function sort()
        
'''
Sugestion by users of Leetcode:
for j in range(n):
    nums1[m+j] = nums2[j]
nums1.sort()
'''