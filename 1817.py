class Solution(object):
    def findingUsersActiveMinutes(self, logs, k):
        """
        :type logs: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        
        
        
        result = list()        
        already = dict()
        for x in range(0, k):
            result.append(0)

        for log in logs:
            already[log[0]] = list()
            
        for log in logs:
            if log[1] not in already[log[0]]:
                already[log[0]].append(log[1])

        
        # 0 : [1,2,3] , 1 : [0,1]
        for key, val in already.items():
            if len(val) != 0:
                result[len(val) - 1] += 1
        
        return result
        
