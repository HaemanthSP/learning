#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
using namespace std;


int main() {
  set<int>s;
  int Q, opt, val;
  cin >> Q;
  for(int i=0; i<Q; i++)
  { cin >> opt >> val;
    switch(opt)
    { case 1:
      { s.insert(val);
        break;
      }
      case 2:
      { s.erase(val);
        break;
      }
      case 3:
      {
        set<int>::iterator itr=s.find(val);
        if(itr == s.end())
          cout << "NO" << endl;
        else
          cout << "Yes" << endl;
      }
    }
  }
  return 0;
}
