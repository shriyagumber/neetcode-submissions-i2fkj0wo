class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        indegrees = [0] * numCourses
        re = []
        map = {}

        for prerequisite in prerequisites:
            before = prerequisite[1]
            after = prerequisite[0]

            indegrees[after] += 1

            if before not in map: map[before] = []
            map[before].append(after)
        

        q = deque()
        tot = 0

        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)
                re.append(i)
                tot += 1

        while q:
            curr = q.popleft()

            if curr not in map: continue
            li = map[curr]
            for i in range(len(li)):
                indegrees[li[i]] -= 1

                if indegrees[li[i]] == 0:
                    q.append(li[i])
                    tot += 1
                    re.append(li[i])
        
        if tot < numCourses: return []
        else: return re





        