#Problem: http://www.usaco.org/index.php?page=viewproblem2&cpid=855

'''
when mixing milk, there are 2 options.
1. give all (m1 -> m2), when m1 < c2-m2. Ex: m1=3, c2=10,m2=5.
3 < 10-5, 3<5. After -> m1=0, m2=8,c2=10.
2. give milk to fullest capacity of next bucket(m1 -> c2-m2), when m1>c2. Ex: m1=12, c2=10,m2=4. c2-m2=6. m1-6. m2+6.
min(m1,c2-m2)

Solution credit: https://usaco.guide/bronze/simulation?lang=py
'''

input_file = open('mixmilk.in')

milk_arr = []
for _ in range(3):
  milk_arr.append([int(i) for i in input_file.readline().split()])
  
for i in range(3):
  cur_index = i%3
  next_index = (i+1)%3
  amount = min(milk_arr[cur_index][1],milk_arr[next_index][0]-milk_arr[next_index][1])
  milk_arr[cur_index][1] -= amount
  milk_arr[next_index][1] += amount

with open('mixmilk.out', 'w') as out:
	for i in range(len(milk_arr)):
		print(milk_arr[i][1], file=out)
