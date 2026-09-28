class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l, r = 0, 0
        temp = []
        while l < m or r < n:
            if l == m:
                temp += nums2[r:]
                break
            if r == n:
                temp += nums1[l:m]
                break
            
            if nums1[l] <= nums2[r]:
                temp.append(nums1[l])
                l += 1
            else:
                temp.append(nums2[r])
                r += 1
        
        nums1[::] = temp