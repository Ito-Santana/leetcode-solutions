class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        root=int(num**(1/2))
        if root**2 == num:
            return True
        return False