class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        m=min(nums1)
        o=10**9
        for i in nums1:
            if i%2!=0 and i<o:
                o=i   
        if o==10**9:
            return True
        for i in nums1:
            if i%2==0 and i<o:
                return False
        return True