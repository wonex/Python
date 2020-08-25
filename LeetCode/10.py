
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def traceback(i,j) -> bool:
            if p is None: return s is None
            if (i,j) in memo: return memo[(i,j)]
            first = len(s) > 0 and p[0] in {s[0], '.'}
            ans = True
            if len(p) - j >= 2 and p[j] == '*':
                ans = first and traceback(i+1, j+2) or traceback(i, j+2)
            else:
                ans = first and traceback(i+1, j+1)
            memo[(i,j)] = ans
            return ans
        return traceback(0,0)
