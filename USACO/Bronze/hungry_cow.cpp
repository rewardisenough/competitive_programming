#include <iostream>
using namespace std;

int main() {
  // set up
  long long N,T; cin >> N >> T;
  long long deliveries[N+1][2];
  
  for(long long i = 0; i < N; i++){
    cin >> deliveries[i][0] >> deliveries[i][1]; 
  }
  deliveries[N][0] = T+1;
  deliveries[N][1] = 0;

  // main part
  long long left_over = 0, total_eat = 0, cur_d = 0, next_d = 0;
  for(long long i = 0; i < N; i++){
    cur_d = deliveries[i][0];
    next_d = deliveries[i+1][0];
    if((deliveries[i][1] + left_over) > (next_d-cur_d)){
      total_eat += (next_d-cur_d);
      if(((deliveries[i][1] + left_over) - (next_d-cur_d)) > 0){
        left_over = (deliveries[i][1] + left_over) - (next_d-cur_d);
      }
      else{
        left_over = 0;
      }
    }
    else{
      total_eat += (deliveries[i][1] + left_over);
      left_over = 0;
    }
  }

  // output
  cout << total_eat << '\n';
}
