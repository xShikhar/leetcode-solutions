class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        time = 0
        max_time = neededTime[0]

        for i in range(1, len(colors)):
            if colors[i - 1] == colors[i]:
                time += min(max_time, neededTime[i])
                max_time = max(max_time, neededTime[i])
            else:
                max_time = neededTime[i]

        return time
