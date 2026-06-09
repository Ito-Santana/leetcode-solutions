class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x_value=int("".join(map(str, digits)))
        output_value = str(x_value+1)
        output_list=[]
        for i in range(0, len(output_value)):
            output_list.append(int(output_value[i]))
        return output_list