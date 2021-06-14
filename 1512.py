class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        length = len(nums)
        result = 0
        
        for idx in range(0, length):
            if idx is length - 1 :
                break
                
            picked = nums[idx]
            for num in range(idx + 1, length):
                if picked is nums[num]:
                    result += 1
        
        return result
            
            
            
        
        
