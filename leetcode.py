# https://leetcode.com/problems/regular-expression-matching/

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not '.' in p and not '*' in p:
            # exact match
            return s == p
        if not s:
            # empty string matches empty pattern or pattern with * of first char
            return not p or (len(p) > 1 and p[1] == '*' and self.isMatch(s, p[2:]))
        if len(p) > 1 and p[1] == '*':
            # match 0 or more of first char
            return self.isMatch(s, p[2:]) or (p[0] == '.' or p[0] == s[0]) and self.isMatch(s[1:], p)
        else:
            # match first char and recurse
            return (p[0] == '.' or p[0] == s[0]) and self.isMatch(s[1:], p[1:])

s = Solution()   
assert not s.isMatch( "aa", "a")
assert s.isMatch( "aa", "a*")
assert s.isMatch( "ab", ".*")