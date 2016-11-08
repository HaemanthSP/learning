#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
  vector<int>::iterator low;
  vector<int> data;
  int N,ele,Q,q,index;
  cin >> N;
  for(int i=0; i<N; i++)
  { cin >> ele;
    data.push_back(ele);
  }
  cin >> Q;
  for(int i=0; i<Q; i++)
  { cin >> q;
    low = lower_bound(data.begin(), data.end(), q);
    index = low - data.begin();
    if(data[index] == q)
      cout << "Yes ";
    else
      cout << "No";
    cout << index+1 <<endl;
  }
  return 0;
}
