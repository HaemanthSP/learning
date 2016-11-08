#include <iostream>
using namespace std;

// Assumption no repeatation of elements in the array.
int main()
{ 
  long a[10] = {1,2,3,4,5,6,7,8,9,10};
  long b[10] = {2,3,4,5,6,7,8,9,10}; 
  int lower, upper, mid;
  lower = 0;
  upper = 9;
 
  // Localize the region.
  while(1)
  { mid = (upper + lower)/2;
    if( a[mid] == b[mid])
     lower = mid;
    else
     upper = mid;
    
    if((upper - lower) <= 3)
      break;
  }

  // Step through the region of 3 elements
  for(int i=lower; i<=upper; i++)
  { if(a[i] == b[i])
      continue;
    else
    { cout << "Result:" << i+1 << endl;
      break;
    }
  }
}
