class Solution:
    def processStr(self, s: str) -> str:
        result = []

        for ch in s:
            if ch.isalpha():
                result.append(ch)

            elif ch == '#':
                result.extend(result)

            elif ch == '%':
                result.reverse()

            elif ch == '*':
                if result:
                    result.pop()

        return "".join(result)