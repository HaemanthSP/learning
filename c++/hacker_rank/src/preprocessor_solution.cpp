#include <iostream>
#include <vector>
#define FUNCTION(name, opt) int  _##name(int a, int b) { return a opt b?a:b ;} 
#define maximum _maximum
#define minimum _minimum
#define io(v) 




using namespace std;

#if defined toStr || defined io || !defined FUNCTION || defined INF
#error Missing preprocessor definitions
#endif 

FUNCTION(minimum, <)
FUNCTION(maximum, >)

int main()
{
/*  int n; cin >> n;
  vector<int> v(n);
  foreach(v, i) {
    io(v)[i];
  }
  int mn = INF;
  int mx = -INF;
  foreach(v, i) {
    minimum(mn, v[i]);
    maximum(mx, v[i]);
  }
  int ans = mx - mn;
  cout << toStr(Result =) <<' '<< ans;
*/
  return 0;
}
