class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x = y = z = False

        for a, b, c in triplets:
            x |= (a == target[0] and b <= target[1] and c <= target[2])
            y |= (a <= target[0] and b == target[1] and c <= target[2])
            z |= (a <= target[0] and b <= target[1] and c == target[2])

            if x and y and z:
                return True
        
        return False
