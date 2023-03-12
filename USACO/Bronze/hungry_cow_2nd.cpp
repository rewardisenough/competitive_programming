#include <iostream>
using namespace std;

int main() {
  long long n,t; cin >> n >> t;
  long long last_d, last_b; cin >> last_d >> last_b;
  long long total_eat = 0;
  long long total_food = last_b;
  long long cur_d = 0 ,cur_b = 0 ,dates = 0;

  for(int i = 0; i < n-1; i++){
    cin >> cur_d >> cur_b;
    dates = cur_d-last_d;
    if(dates>total_food) total_eat += total_food, total_food -= total_food;
    else total_eat += dates, total_food -= dates;
    total_food += cur_b;
    last_d = cur_d;
  }
  // check last n to t.
  if(t-last_d+1 > total_food) total_eat += total_food;
  else total_eat += t-last_d+1;

  //output
  cout << total_eat << "\n";
}
