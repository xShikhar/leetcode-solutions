class Solution(object):
    def merge(self, interval):
        result = []
        interval.sort()
        current  = interval[0]

        for i in range(1,len(interval)):
            if current[1] >= interval[i][0]:
                current[1] = max(current[1],interval[i][1])
            
            else:
                result.append(current)
                current = interval[i]
        result.append(current)
        return result
