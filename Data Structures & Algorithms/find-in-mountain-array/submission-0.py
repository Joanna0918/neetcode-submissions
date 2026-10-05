class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()

        # Find the peak
        l, r = 1, length - 2
        while l <= r:
            m = (l + r) // 2
            left, mid, right = mountainArr.get(m - 1), mountainArr.get(m), mountainArr.get(m + 1)

            if left < mid < right: # left portion
                l = m + 1
            elif left > mid > right: # right portion
                r = m - 1
            else:
                break
        
        # Find in the left portion
        l, r = 0, m
        while l <= r:
            middle = (l + r) // 2
            if mountainArr.get(middle) < target:
                l = middle + 1
            elif mountainArr.get(middle) > target:
                r = middle - 1
            else:
                return middle
        
        # Find in the right portion
        l, r = m, length - 1
        while l <= r:
            middle = (l + r) // 2
            if mountainArr.get(middle) < target:
                r = middle - 1
            elif mountainArr.get(middle) > target:
                l = middle + 1
            else:
                return middle
        
        return -1