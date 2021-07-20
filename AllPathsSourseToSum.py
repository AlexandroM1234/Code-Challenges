class Solution:
    def allPathsSourceTarget(self, graph):
        q = [[0]]
        output = []
        target = len(graph) - 1

        while len(q):
            node = q.pop(0)

            if node[-1] == target:
                output.append(node)
            else:
                for neighbor in graph[node[-1]]:
                    print(neighbor)
                    q.append(node + [neighbor])
        return output
