class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        map = {}
        maxFreq = 0
        numFreq = 0

        # getting the maxFreq and numFreq information
        for i in range(len(tasks)):
            ch = tasks[i]

            if ch in map: map[ch] += 1
            else: map[ch] = 1

            if map[ch] > maxFreq:
                maxFreq = map[ch]
                numFreq = 1
            elif map[ch] == maxFreq:
                numFreq += 1
        
        partitions = maxFreq - 1
        available = partitions * (n - numFreq + 1)
        pending = len(tasks) - (maxFreq * numFreq)
        idle = max(0, available - pending)

        return len(tasks) + idle
        