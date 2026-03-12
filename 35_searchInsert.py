class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        left,right = 0, n-1
        first_index = -1
        while left<=right:
            mid = (left+right)//2
            if nums[mid] >= target:
                first_index = mid
                right = mid -1
            else:
                left = mid+1
        return first_index if first_index != -1 else n
