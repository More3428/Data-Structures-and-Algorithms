class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in range(len(nums)):
            if nums[i] > 0 or nums[i] < 0:
                temp = nums[i]
                nums[i] = nums[count]
                nums[count] = temp
                count += 1

"""

TimeComplexity: O(n)
SpaceComplexity:O(1)

----------------------------------------
Given an integer array nums, 
move all 0's to the end of it 
while maintaining the relative order 
of the non-zero elements.
--------------------------

"""