class Solution:
    def networkDelayTime(self, times, N: int, K: int) -> int:
        distances = {}
        visited = set()
        
        distances[K] = 0
        
        graph = {}

        for (u, v, w) in times:
            vertex = (v, w)
            if u in graph:
                graph[u].append(vertex)
            else:
                graph[u] = [vertex]

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
        
        while len(visited) != len(distances) - 1:
            
            v = None
            dist_to_v = None
            for v_candidate in distances:
                
                dist_candidate = distances[v_candidate]
                if isGreaterDist(dist_to_v, dist_candidate) and v_candidate not in visited:
                    dist_to_v = dist_candidate
                    v = v_candidate
            
            visited.add(v)
            if v not in graph:
                continue

            neighbors = graph[v]

            for (neighbor, w) in neighbors:
                if neighbor not in visited:
                        if isGreaterDist(distances[neighbor], addDistance(distances[v], w)):
                            distances[neighbor] = addDistance(distances[v], w)

                
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