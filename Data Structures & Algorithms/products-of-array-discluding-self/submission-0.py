class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post = [1], [1]

        for i in range(1, len(nums)):
            pre.append(pre[len(pre)-1] * nums[i-1])
            # print(pre)

        for j in range(len(nums) - 2, -1, -1):
            post.append(post[len(post)-1] * nums[j+1])
            # print(post)

        res = []

        for i in range(len(nums)):
            res.append(pre[i] * post[len(nums)-1-i])
            # print(res)
        
        return res