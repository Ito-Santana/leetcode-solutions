class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer=[]
        for i in range(1,n+1):
            flag_div_3 = (i % 3 == 0)
            flag_div_5 = (i % 5 == 0)
            
            if flag_div_3 and flag_div_5:
                answer.append("FizzBuzz")
            elif flag_div_3:
                answer.append("Fizz")
            elif flag_div_5:
                answer.append("Buzz") 
            else:
                answer.append(str(i))
        return answer