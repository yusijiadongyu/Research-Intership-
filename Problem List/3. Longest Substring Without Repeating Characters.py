class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        result = 0
        tmp = 0
        for i in range(len(s)):
            end = i
            if end == start:
                continue
            flag = 0
            # this is to evaluate if an element exists in [i,j], which is not effcient with O(n^2) complexity
            for j in range(end - 1, start - 1, -1):
                if s[j] == s[end]:
                    result = max(result, end - start)
                    start = j + 1
                    flag = 1
                    tmp = 0
                    break
            result = max(result, end - start + 1)
        if result == 0 and len(s) > 0:
                result = len(s)
        return result



## method 2: with complexity O(n)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maps = {}
        l = len(s)
        start = end = 0
        res = 0
        for i in range(l):
            if s[i] in maps:
                end = end + 1
                start = max(start, maps[s[i]])
                maps[s[i]] = i + 1
            else:
                end = end + 1
                maps[s[i]] = i + 1
            res = max(res, end - start)
        return res
                