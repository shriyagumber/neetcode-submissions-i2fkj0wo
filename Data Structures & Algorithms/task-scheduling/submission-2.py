class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        map = [0] * 26
        maxFreq = 0
        numFreq = 0

        # getting the maxFreq and numFreq information
        for i in range(len(tasks)):
            ch = tasks[i]
            idx = ord(ch)-ord('A')

            map[idx] += 1

            if map[idx] > maxFreq:
                maxFreq = map[idx]
                numFreq = 1
            elif map[idx] == maxFreq:
                numFreq += 1
        
        partitions = maxFreq - 1
        available = partitions * (n - numFreq + 1)
        pending = len(tasks) - (maxFreq * numFreq)
        idle = max(0, available - pending)

        return len(tasks) + idle
        