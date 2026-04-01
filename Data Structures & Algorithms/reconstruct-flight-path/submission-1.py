class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        map = {}
        n = len(tickets)

        for ticket in tickets:
            orig = ticket[0]
            dest = ticket[1]

            if orig not in map: map[orig] = []
            map[orig].append(dest)

        for key in map.keys(): map[key].sort()

        res = ["JFK"]

        def dfs(curr):
            # base case
            if len(res) == n+1:
                return True
            if curr not in map:
                return False

            # logic
            li = list(map[curr])
            for i, next_place in enumerate(li):

                # removing from this list, so that when it is encountered in next pass, 
                # then 
                map[curr].pop(i)
                res.append(next_place)

                if dfs(next_place): return True

                map[curr].insert(i, next_place)
                res.pop()
            
            return False

        dfs("JFK")

        return res
                



            





        