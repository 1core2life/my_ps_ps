class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        
        while(True):
            if n is 1:
                break
                
            if n % 2 is 0:
                result += n/2
                n /= 2
                
            elif n % 2 is 1:
                result += (n-1)/2
                n -= 1
                n /= 2
                n += 1
        
        return result
            
                
