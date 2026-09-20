class CountSquares:

    def __init__(self):
        self.ptCounts = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.ptCounts[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point

        for (x, y), diagonalCount in self.ptCounts.items():

            # Must be a diagonal point of a square
            if abs(py - y) != abs(px - x) or x == px or y == py:
                continue

            horizontalCount = self.ptCounts.get((x, py), 0)
            verticalCount = self.ptCounts.get((px, y), 0)

            res += (
                diagonalCount * horizontalCount * verticalCount
            )

        return res