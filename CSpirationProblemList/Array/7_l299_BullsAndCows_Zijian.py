class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        counter = collections.Counter()
        bull, cow = 0, 0
        for c in secret:
            counter[c] += 1
        for cs, cg in zip(secret, guess):
            if cs == cg:
                bull += 1
                if not counter[cg]:
                    cow -= 1
                else:
                    counter[cg] -= 1
            else:
                if counter[cg] > 0:
                    cow += 1
                    counter[cg] -= 1
        return '{}A{}B'.format(bull,cow)
