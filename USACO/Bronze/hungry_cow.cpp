#include <iostream>
// using namespace std;

// int main() {
//   int n,t; cin >> n >> t;
//   int last_d, last_b; cin >> last_d >> last_b;
//   int total_eat = 0;
//   int total_food = last_b;
//   int cur_d,cur_b,dates;

//   for(int i = 0; i < n-1; i++){
//     cin >> cur_d >> cur_b;
//     dates = cur_d-last_d;
//     if(dates>total_food) total_eat += total_food, total_food -= total_food;
//     else total_eat += dates, total_food -= dates;
//     total_food += cur_b;
//     last_d = cur_d;
//   }
//   // check last n to t.
//   if(t-last_d+1 > total_food) total_eat += total_food;
//   else total_eat += t-last_d+1;

//   //output
//   cout << total_eat << "\n";
// }

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
