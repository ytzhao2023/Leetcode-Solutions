class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        curRestGas = 0
        totalRestGas = 0
        startIndex = 0
        
        for i in range(len(gas)):
            curRestGas += gas[i] - cost[i]
            totalRestGas += gas[i] - cost[i]
            
            if curRestGas < 0:
                startIndex = i + 1
                curRestGas = 0
                
        if totalRestGas < 0:
            return -1
        
        return startIndex