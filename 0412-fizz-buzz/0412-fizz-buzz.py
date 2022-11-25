class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        my_numbers = []
        for number in range(1, n+1):
            if (number % 3 == 0) and (number % 5 == 0):
                my_numbers.append("FizzBuzz")
            elif (number % 3 == 0):
                my_numbers.append("Fizz")
            elif (number % 5 == 0):
                my_numbers.append("Buzz")
            else:
                my_numbers.append(f"{number}")
            
        return my_numbers;