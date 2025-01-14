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
            for j in range(end - 1, start - 1, -1):
                if s[j] == s[end]:
                    result = max(result, end - start)
                    start = j + 1
                    flag = 1
                    tmp = 0
                    break
            # if flag == 0:
            #     tmp = tmp +  1
        return result
        