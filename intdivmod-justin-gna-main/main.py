# Justin G. Fr. Michael Goetz CSS
# 2/19/2021
# Int Division and Mod Functions: A program that does integer division and modulous operation without using the built in functions from python

def int_div(n, m):
  # using repeated subtraction to find how many times the divisor goes into the dividend evenly
  # the loop just keeps subtracting the m value and stops when answer is negative or 0
  count = 0
  answer = n - m
  while answer >= 0:
    count += 1
    answer = answer - m

  return count

def my_mod(n, m):
  answer = 0
  answer = n - m
  while answer >= m:
    answer = answer - m

  return answer
  
dividend = int(input("enter the dividend: "))
divisor = int(input("enter the divisor: "))

quotient = int_div(dividend, divisor)
remainder = my_mod(dividend, divisor)

print("quotient:", quotient)
print("remainder:", remainder)
print(dividend // divisor )
print(dividend % divisor)