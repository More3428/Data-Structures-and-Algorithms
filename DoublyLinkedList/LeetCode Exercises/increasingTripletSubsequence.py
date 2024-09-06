class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        minOne = float('inf')
        minTwo = float('inf')
        for i in range(len(nums)):
            if nums[i] < minOne:
                minOne = nums[i]
            if nums[i] > minOne:
                minTwo = min(nums[i], minTwo)
            if nums[i] > minTwo:
                return True       
        return False
"""
TimeComplexity: O(n)
SpaceComplecity: O(1)
---------------------------------------------------------
Given an integer array nums, 
return true if there exists a triple of indices (i, j, k) 
such that i < j < k and nums[i] < nums[j] < nums[k]. 
If no such indices exists, return false.
----------------------------------------
"""