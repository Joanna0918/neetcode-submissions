class CountSquares:

    def __init__(self):
        self.pointCount = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.pointCount[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        qx, qy = point[0], point[1]
        res = 0
        for (x, y), diagonalCount in self.pointCount.items():
            if abs(qy - y) != abs(qx - x) or x == qx or y == qy:
                continue
            
            if (x, qy) in self.pointCount and (qx, y) in self.pointCount:
                res += diagonalCount * self.pointCount[(x, qy)] * self.pointCount[(qx, y)]
        return res