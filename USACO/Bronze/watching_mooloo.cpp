#include <iostream>
using namespace std;
int main() {
  // set up
  long long N,K; cin >> N >> K;
  long long last_d = 0, cur_d = 0, total_amount = 1+K;
  cin >> last_d;

  // main part
  for(int i = 0; i < N-1; i++){
    cin >> cur_d;
    // conditional statements
    if((cur_d-last_d)>(1+K)){
      total_amount += (1+K);
    }
    else{
      total_amount += (cur_d-last_d);
    }
    // switch last_d with cur_d
    last_d = cur_d;
  }

  // output
  cout << total_amount << '\n';
}
