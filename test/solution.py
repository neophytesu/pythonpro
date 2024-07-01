import copy
import queue
from collections import defaultdict
from typing import List


class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        g = defaultdict(list)
        for x, y, z in edges:
            g[x].append((y, z))
            g[y].append((x, z))
        visited = {0}
        ans = 0

        def dfs(u: int, time: int, value: int) -> None:
            if u == 0:
                nonlocal ans
                ans = max(ans, value)
            for v, dist in g[u]:
                if time + dist <= maxTime:
                    if v not in visited:
                        visited.add(v)
                        dfs(v, time + dist, value + values[v])
                        visited.discard(v)
                    else:
                        dfs(v, time + dist, value)

        dfs(0, 0, values[0])
        return ans
