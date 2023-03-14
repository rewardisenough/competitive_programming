#include <iostream>
using namespace std;


int main() {
  // inputs
  int N; cin >> N;
  
  string str; cin >> str;
  
  int E[N];
  for(int i = 0; i < N; i++){
    cin >> E[i];
  }

  // find leader index(at least 1)
  int g_leader = 0, h_leader = 0;
  int g_total = 0, h_total = 0;
  if(E[str.find('G')]-1 >= str.find_last_of('G')){ 
    g_leader = str.find('G');
    g_total++;
  }
  if(E[str.find('H')]-1 >= str.find_last_of('H')){ 
    h_leader = str.find('H');
    h_total++;
  }

  // total
  if(h_leader>0){
    for(int i = 0; i < h_leader; i++){
      if(E[i]-1 >= h_leader) g_total++;
    }
  }
  else{
    for(int i = 0; i < g_leader; i++){
      if(E[i]-1 >= g_leader) h_total++;
    }
  }

  // output
  cout << g_total * h_total << '\n';
}
  
