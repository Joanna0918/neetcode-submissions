class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        I, J, K = False, False, False

        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            
            if triplet[0] == target[0]:
                I = True
            if triplet[1] == target[1]:
                J = True
            if triplet[2] == target[2]:
                K = True
        
        return I and J and K