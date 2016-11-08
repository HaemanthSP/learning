#include <iostream>
#include <deque> 
using namespace std;

int main()
{ int t;
  cin >> t;
  while(t>0) 
  { int n,k;
    cin >> n >> k;
    int i;
    int ele;
    deque<int> data;
    for(i=0;i<n;i++)
    { cin >> ele;
      data.push_back(ele);
      if(data.size() == k)
      {
        deque<int> temp;
        temp = data;
      	make_heap(temp.begin(), temp.end());
      	cout << temp.front() << " ";
        data.pop_front();
      }
    }
    t--;
  }
  return 0;
}
