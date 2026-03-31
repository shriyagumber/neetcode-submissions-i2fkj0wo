class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        totGas = 0
        currGas = 0
        idx = 0

        for i in range(n):
            totGas += (gas[i] - cost[i])
            currGas += (gas[i] - cost[i])

            if currGas < 0:
                idx = i+1
                currGas = 0
        
        if totGas < 0: return -1

        return idx
        