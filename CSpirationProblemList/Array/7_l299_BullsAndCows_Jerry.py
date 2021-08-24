"""
Discription: 
Created Date: Monday, August 23rd 2021, 7:28:14 pm
Author: Jerrio Zhang
-----
Last Modified: Monday, 08 23rd 2021, 7:29:04 pm
Modified By: Jerrio Zhang
-----
Copyright (c) 2021 IceWould Information Technology Co., Ltd.
-----
HISTORY:
Date      	By	Comments
----------	---	----------------------------------------------------------
"""
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a = 0
        b = 0
        r_secret = []
        r_guess = []
        for i in range(len(secret)):
            r_secret.append(secret[i])
            r_guess.append(guess[i])

        for i in range(len(guess)):
            if guess[i] == secret[i]:
                a += 1
                r_secret.remove(guess[i])
                r_guess.remove(guess[i])

        for i in range(len(r_guess)):
            if r_guess[i] in r_secret:
                b += 1
                r_secret.remove(r_guess[i])
                
        return "{}A{}B".format(a,b)