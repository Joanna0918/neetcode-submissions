class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        q = deque()

        for a in asteroids:
            alive = True
            while q and q[-1] > 0 and a < 0:
                b = q[-1]

                if abs(b) < abs(a):
                    # previous asteroid destroyed
                    q.pop()
                    # a is still alive, so check previous asteroid
                    continue

                elif abs(b) == abs(a):
                    # both destroyed
                    q.pop()
                    alive = False
                    break

                else:
                    # current asteroid destroyed
                    alive = False
                    break

            if alive:
                q.append(a)

        return list(q)