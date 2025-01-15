class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        maps = {
                "I":1,
                "IV":4,
                "V":5,
                "IX":9,
                "X":10,
                "XL":40,
                "L":50,
                "XC":90,
                "C":100,
                "CD":400,
                "D":500,
                "CM":900,
                "M":1000
        }   
        res = 0
        n = len(s)
        i = 0
        while i < n-1:
            if s[i]+s[i+1] in maps:
                res = res + maps[s[i]+s[i+1]]
                i = i + 2
            else:
                res = res + maps[s[i]]
                i = i + 1
        if i < n:
            res = res + maps[s[i]]
        return res