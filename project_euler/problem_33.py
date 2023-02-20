# arrays
correct_num = []
correct_denom = []
start_nums = [12,23,34,45,56,67,78,89]

#helper functions
def first_digit(num):
  return int(num/10)

def second_digit(num):
  return num%10

def one_time(numerator,threshold):
  start_num = numerator
  while(start_num<threshold):
    for num in range(1,10): #1...9
      start_denom = second_digit(start_num) * 10 + num
      if(start_num/start_denom == (first_digit(start_num))/second_digit(start_denom)):
        correct_num.append(start_num)
        correct_denom.append(start_denom)
    start_num += 1


# driver function
for numerator in start_nums:
  threshold = (first_digit(numerator)+1)*10
  one_time(numerator,threshold)

# results
print(correct_num)
print(correct_denom)
import numpy as np
import math
gcd = math.gcd(np.prod(correct_num),np.prod(correct_denom))
print(f"Answer:{np.prod(correct_denom)/gcd}") # simplest form of denominator
