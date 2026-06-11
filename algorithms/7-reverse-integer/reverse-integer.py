class Solution:
    def reverse(self, x: int) -> int:
        signal = False
        if x < 0:
            signal = True
            x = x * (-1)
        
        x_arr = str(x)
        i = len(x_arr)
        return_list = [None] * i
        p = i - 1
        sum = 0
        
        for n in range(0, len(x_arr)):
            return_list[p] = int(x_arr[n])
            p -= 1
            
        for v in range(0, len(return_list)):
            sum = sum + (return_list[v] * (10 ** (len(return_list) - v - 1)))
            
        ans = sum * (-1) if signal else sum

        if -2**31 <= ans <= (2**31)-1:
            return ans
        return 0