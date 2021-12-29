class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        i, j = 0, len(num) - 1
        while i < j:
            if num[i] == '6' and num[j] == '9' \
            or num[i] == '9' and num[j] == '6' \
            or num[i] == '8' and num[j] == '8' \
            or num[i] == '1' and num[j] == '1' \
            or num[i] == '0' and num[j] == '0':
                i = i + 1
                j = j - 1
            else:
                return False
        if i == j:
            return num[i] == '8' or num[i] == '1' or num[i] == '0'
        return True
                
