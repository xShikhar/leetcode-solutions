from collections import defaultdict
class Solution(object):


    def groupAnagrams(self, strs):
        result = []
        anagram = defaultdict(list)

        for i in strs:
            sorted_str = tuple(sorted(i))
            anagram[sorted_str].append(i)
        
        for i in anagram:
            result.append(anagram[i])
        return result
