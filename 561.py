class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        result = 0
        for i in range(0, len(nums)/2):
            result += min(nums[i*2], nums[i*2+1])
        
        return result
