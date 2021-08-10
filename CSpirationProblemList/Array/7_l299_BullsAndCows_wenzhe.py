class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
        
        secret_dict = {}
        for i in secret:
            if i in secret_dict:
                secret_dict[i] += 1
            else:
                secret_dict[i] = 1
        
        cows = 0
        for i in guess:
            if i in secret_dict and secret_dict[i] > 0:
                cows += 1
                secret_dict[i] -= 1
        cows -= bulls
        return str(bulls) + "A" + str(cows) + "B"