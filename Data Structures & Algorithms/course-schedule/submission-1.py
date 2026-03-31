class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        indegree = [0] * numCourses
        map = {}

        for prerequisite in prerequisites:
            after = prerequisite[0]
            before = prerequisite[1]

            indegree[after] += 1

            if before not in map:
                map[before] = []
            map[before].append(after)


        tot = 0
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
                tot += 1
        
        while q:

            curr = q.popleft()
            if curr not in map: continue
            li = map[curr]

            for i in range(len(li)):
                indegree[li[i]] -= 1

                if indegree[li[i]] == 0:
                    q.append(li[i])
                    tot += 1
        

        if tot == numCourses: return True
        else: return False


                
                
        