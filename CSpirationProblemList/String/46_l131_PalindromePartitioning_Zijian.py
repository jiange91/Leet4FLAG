class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def helper(s):
            ans = []
            for i in range(1, len(s)+1):
                if s[:i] == s[i-1::-1]:
                    ans += [[s[:i]] + rest for rest in helper(s[i:])]
            return ans or [[]]
        return helper(s)

# With DP
class Solution:
def partition(self, s: str) -> List[List[str]]:
@cache
def helper(i, j, s):
    ans = []
    for k in range(i+1, j+2):
        if s[i:k] == s[k-1:-1*(len(s) - i + 1):-1]:
            ans += [[s[i:k]] + rest for rest in helper(k,j,s)]
    return ans or [[]]
return helper(0, len(s)-1, s)