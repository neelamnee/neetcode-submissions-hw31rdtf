from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []

        for t in tokens:
            if t not in ["+", "-", "*", "/"]:
                s.append(int(t))
            else:
                a = s.pop()
                b = s.pop()
                
                if t == "+":
                    s.append(b + a)
                elif t == "-":
                    s.append(b - a)
                elif t == "*":
                    s.append(b * a)
                else:
                    s.append(int(b / a))

        return s.pop()