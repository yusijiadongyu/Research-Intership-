class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        maps = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        res = []
        tmp = []
        for i in range(len(digits)):
            s = maps[digits[i]]
            if not res:
                for j in range(len(s)):
                    res.append(s[j])
            else:
                tmp = res
                res = []
            for j in range(len(s)):
                for k in range(len(tmp)):
                    res.append(tmp[k] + s[j])
        return res
        