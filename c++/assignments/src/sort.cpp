#include<iostream>

using namespace std;

int main()
{
  int i, index, j=0, len;
  bool sorted = false;
  cout << "Enter the length of data" << endl;
  cin >> len;
  int* data = new int[len];
  int min=0;

  cout << "Enter the data" << endl; 
  for(int i=0; i<len; i++)
    cin >> data[i];
  while(!sorted)
  { index = j;
    min = data[j];
    for(int i = j; i<len; i++)
    {
      if(data[i] < min)
      { index = i;
        min = data[i];
      }
    }
    swap(data[index], data[j]);
   
    j++; 
    if(j == len)
      sorted = true;
  }
  for(int i=0; i<len; i++)
    cout << data[i];
  cout << endl;
}
