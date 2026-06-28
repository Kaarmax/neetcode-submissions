class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", '')
        s = s.lower()
        L = list(s)
        S = []
        for i in L:
            if i.isalnum():
                S.append(i)
        for i in range(int(len(S)/2)):
            if S[i] != S[len(S) - i - 1]:
                return False
        else:
            return True