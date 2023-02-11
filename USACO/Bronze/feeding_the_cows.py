# solution credit:https://www.youtube.com/watch?v=dWbMfohtudg

'''
most important parts:

1. i-last_g >k
This ensures that we are skipping cows that are able to reach the latest patch. For example, i = 7, last_g = 2, k = 3. Then, 7-2>3. Therefore, cow at i=7 are not able to reach last_g.

2. min(i+k,n-1)
i+k means the position of the latest patch. Therfore, last_g oor last_h needs to be updated at i+k. However, if i+k is out of bounds, then we just say n-1 which is the last position of the output_str.

3. if output_str[last_g] != '.'
However, if output_str is already occupied, then you subtract 1 more from n-1 thus equals n-2. You can see that this is only possible when the last part of string is either GH or HG and k=1. 

For example, 'HHG', k=2. First, '..H', you might think that G should go into n-2. However, if it's 'HHHG', then '..H.', thus G at n-1 is possible. even if it's 'GHHG', results would be '..GH'. This pattern works when k>1.
'''


t = int(input())

for _ in range(t):
  # set up
  n,k = [int(i) for i in input().split()]
  
  input_str = input()
  input_str = [input_str[i] for i in range(len(input_str))] # seperates letter of the string into elements of an array
  
  output_str = ['.' for _ in range(n)]

  # main
  last_g= -k-1 # if i==0, then i-(-k-1)>k. Still works.
  last_h = -k-1 # if i==0, then i-(-k-1)>k. Still works.
  count = 0

  for i in range(n):
    if(input_str[i]=='G' and i-last_g > k):
      last_g = min(i+k,n-1)
      if output_str[last_g] != '.':
        last_g -= 1
      output_str[last_g] = 'G'
      count+=1
      
    elif(input_str[i]=='H' and i-last_h>k):
      last_h = min(i+k,n-1)
      if output_str[last_h] != '.':
        last_h -= 1
      output_str[last_h] = 'H'
      count+=1

  # output
  print(count)
  print(output_str)
