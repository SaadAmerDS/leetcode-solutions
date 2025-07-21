# LeetCode 1957. Delete Characters to Make Fancy String
# Python | O(n) Time | Clean Greedy Solution

class Solution:
    def makeFancyString(s: str) -> str:
        result = []
        for c in s:
            if len(result) >= 2 and result[-1] == result[-2] == c:
                continue
            result.append(c)
        return ''.join(result)
