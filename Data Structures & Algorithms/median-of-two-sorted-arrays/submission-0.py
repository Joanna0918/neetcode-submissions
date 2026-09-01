class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) <= len(nums2):
            A, B = nums1, nums2
        else:
            A, B = nums2, nums1

        total = len(nums1) + len(nums2)
        half = total // 2
        
        l, r = 0, len(A) - 1

        while True:
            i = (l+r) // 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float('-inf')
            Aright = A[i+1] if i < (len(A)-1) else float('inf')
            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[j+1] if j < (len(B)-1) else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 1:
                    return min(Bright, Aright)
                else:
                    return (min(Aright, Bright) + max(Aleft, Bleft)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
