class Solution:
    def countBits(self, n: int) -> List[int]:
        offset = 1
        res = [0]

        for i in range(1, n + 1):
            if i == offset * 2:
                offset = i
            res.append(1 + res[i - offset])
        
        return res