class Solution:
    def isValid(self, s: str) -> bool:
        round_ = "()"
        curly = "{}"
        square = "[]"
        L = [round_, curly, square]
        
        for i in range(len(s)):
            a = 0
            while a+1 < len(s):
                if s[a] + s[a+1] in L:
                    s = s[:a] + s[a+2:] 
                a += 1

        if s == "":
            return True
        else:
            return False
            
                


