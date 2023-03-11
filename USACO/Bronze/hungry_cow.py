N, T = map(int, input().split())
deliveries = [tuple(map(int, input().split())) for _ in range(N)] + [(T+1, 0)]


left_over, total_eat = 0,0
cur_d, next_d = 0,0

for i in range(len(deliveries)-1):
  cur_d = deliveries[i][0]
  next_d = deliveries[i+1][0]
  if((deliveries[i][1] + left_over) > (next_d-cur_d)):
    total_eat += (next_d-cur_d)
    left_over = max(0, (deliveries[i][1] + left_over) - (next_d-cur_d))
  else:
    total_eat += deliveries[i][1] + left_over
    left_over = 0

print(total_eat)
