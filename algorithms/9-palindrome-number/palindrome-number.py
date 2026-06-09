class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_list = list(str(x))
        end = len(x_list) - 1
        reorder_list = list(x_list)
        for i in range(0, len(x_list)):
            reorder_list[end] = x_list[i]
            end -= 1
        if x_list == reorder_list:
            return True
        else:
            return False
