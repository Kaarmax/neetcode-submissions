class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        l = []

        for i in tokens:
            if i == "+":
                l.append(l.pop() + l.pop())
            elif i == "-":
                a, b = l.pop(), l.pop()
                l.append(b - a)
            elif i == "*":
                l.append(l.pop() * l.pop())
            elif i == "/":
                a, b = l.pop(), l.pop()
                l.append(int(float(b) / a))
            else:
                l.append(int(i))
        
        return l[0]


