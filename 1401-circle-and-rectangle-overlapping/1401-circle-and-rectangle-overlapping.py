class Solution:
    def checkOverlap(self, r: int, xc: int, yc: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        i = max(x1, min(xc, x2))
        j = max(y1, min(yc, y2))
        return (xc - i) ** 2 + (yc - j) ** 2 <= r ** 2
