s = "aab"

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
# return result
print(result)