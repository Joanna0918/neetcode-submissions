class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1

        while r - l + 1 > k:
            left_dist = abs(arr[l] - x)
            right_dist = abs(arr[r] - x)

            if left_dist <= right_dist:
                # On a tie, keep the smaller value arr[l]
                r -= 1
            else:
                l += 1

        return arr[l:r + 1]
