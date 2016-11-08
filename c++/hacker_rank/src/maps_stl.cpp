#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <algorithm>
using namespace std;


int main() {
  map<string,int>s;
  string name;
  int Q, opt, mark;
  cin >> Q;
  for(int i=0; i<Q; i++)
  { cin >> opt; 
    switch(opt)
    { case 1:
      { cin >> name >> mark;
        map<string,int>::iterator itr=s.find(name);
        if(itr == s.end())
          s.insert(make_pair(name, mark));
        else
          s[name] += mark;
        break;
      }
      case 2:
      { cin >> name;
        s.erase(name);
        break;
      }
      case 3:
      { cin >> name;
                cout << s[name] << endl;
      }
    }
  }
  return 0;
}
