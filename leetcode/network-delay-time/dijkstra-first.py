class Solution:
    def networkDelayTime(self, times, N: int, K: int) -> int:
        distances = {}
        pathes = {}
        visited = set()
        
        distances[K] = 0
        pathes[K] = []
        
        for (u, v, w) in times:
            if u != K:
                distances[u] = None
            if v != K:
                distances[v] = None
        if len(distances) < N:
            return -1 
        def isGreaterDist(a, b):
            if a == None and b == None:
                return False
            if a == None:
                return True
            if b == None:
                return False
            return a > b
        
        def addDistance(a, b):
            if a == None:
                return b
            if b == None:
                return None
            return a + b
        
        i = 0
        while len(visited) != len(distances) - 1:
            
            v = None
            dist_to_v = None
            for v_candidate in distances:
     
                if isGreaterDist(dist_to_v, distances[v_candidate]) and v_candidate not in visited:
                    dist_to_v = distances[v_candidate]
                    v = v_candidate
                    
            for (a, b, w) in times:

                if b != v and a == v and b not in visited:
                    u = b
                else:
                    continue
                
                if isGreaterDist(distances[u], addDistance(distances[v], w)):
                    distances[u] = addDistance(distances[v], w)
                
            i += 1
            visited.add(v)
            

        max_dist = None
            
        for v in distances:
            if distances[v] == None:
                return -1
            if max_dist == None or distances[v] > max_dist:
                max_dist = distances[v]

        return max_dist
            

sol = Solution()

r = sol.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 3, 2)

print(r)