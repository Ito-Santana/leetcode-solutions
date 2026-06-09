class Solution:
    def addBinary(self, a: str, b: str) -> str:
        binary_array=[]
        sum_value=int(a, 2)+int(b,2)
        if sum_value==0:
            return '0'
        while sum_value > 0 :
            binary_array.append(str(sum_value%2))
            sum_value//=2

        return "".join(binary_array[::-1])