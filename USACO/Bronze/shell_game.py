# problem: http://www.usaco.org/index.php?page=viewproblem2&cpid=891

# Solution credit: https://usaco.guide/bronze/simulation?lang=py

input_file = open('shell.in','r') # read the file

N = int(input_file.readline()) # read only the first line

correct = [0,0,0] # this array's position doesn't change
position_arr = [1,2,3] # starting position of the shells, this array's position changes in loop

for _ in range(N): 
  a,b,g = [int(i)-1 for i in input_file.readline().split()] #read one line and split every word by space(Default)
  position_arr[a],position_arr[b] = position_arr[b],position_arr[a] # swap a and b
  correct[position_arr[g]] += 1 # the number of shell's position in the correct array gets incremmented.

print(max(correct), file=open('shell.out','w')) # write the output file
