class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = set()
        for i in nums:
            if i not in dup:
                dup.add(i)
            else:
                return True
        return False