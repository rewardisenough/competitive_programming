'''
to increase m by k: duplicate each line by k times.
to increase n by k: duplicate letter in each line by k times.(in order)
'''

input_file = open('cowsignal.in')

m,n,k = [int(i) for i in input_file.readline().split()]

arr = [(i).replace("\n","") for i in input_file.readlines()]

final_arr = []

for str in arr:
  temp_str = ""
  for i in range(len(str)):
    temp_str += str[i] * k
  for _ in range(k):
    final_arr.append(temp_str)

with open('cowsignal.out', 'w') as out:
	for str in final_arr:
		print(str, file=out)
