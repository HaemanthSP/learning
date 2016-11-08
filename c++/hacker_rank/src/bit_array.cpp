#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
using namespace std;

int main() {
   long int N, S, P, Q , prev, curr;
   cin >> N >> S >> P >> Q;
   set<long int> s;
   prev = S;
   s.insert(prev);
   for(long int i=1; i<N; i++)
   { curr = ((prev * P) + Q) % 2147483648;
     s.insert(curr);
     prev = curr;
   }
   cout << s.size();
   return 0;
}
