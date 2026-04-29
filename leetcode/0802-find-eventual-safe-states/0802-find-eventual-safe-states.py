class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        color = [0 for _ in range(len(graph))]
        
        res = []
        def topsort(node):

            if color[node] == 1:
                return False

            color[node] = 1
            for neighbor in graph[node]:
                if color[neighbor] == 2:
                    continue
                if not topsort(neighbor):
                    return False
            color[node] = 2
            res.append(node)
            return True

        for i in range(len(graph)):
            if color[i] != 0:#already processed
                continue
            topsort(i)
        res.sort()
        return res