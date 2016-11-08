#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int BoxesCreated,BoxesDestroyed;

class Box
{
  // The class should have the following functions : 
  public:
  int l;
  int b;
  int h;
  // Constructors: 
  Box()
  { l = 0;
    b = 0;
    h = 0;
    BoxesCreated++;
  }
 
  Box(int x,int y,int z)
  { l = x;
    b = y;
    h = z;
    BoxesCreated++;
  }
  Box(Box& bx)
  { l = bx.l;
    b = bx.b;
    h = bx.h;
    BoxesCreated++;
  }
  // Destructor
  ~Box()
  { BoxesDestroyed++;
  }

  int getLength()
  { return l;
  } 
  int getBreadth ()
  { return b;
  }
  int getHeight ()
  { return h;
  }
  long long CalculateVolume() 
  { long long vol;
    vol = l * b * h;
    return vol;
  }
  
  bool operator<(Box &bx)
  {
    if ((l < bx.l) || (b < bx.b && l == bx.l) || (h < bx.h && b == bx.b && l == bx.l))
      return true;
    else
      return false; 
  }

};

ostream& operator<< (ostream &output, Box B)
{ output << B.l << " " << B.b << " " << B.h;
  return output;
}
  
void check2()
{
  int n;
  cin>>n;
  Box temp;
  for(int i=0;i<n;i++)
    {
    int type;
    cin>>type;
    if(type ==1)
        {
          cout<<temp<<endl;
        }
        if(type == 2)
        {
            int l,b,h;
            cin>>l>>b>>h;
            Box NewBox(l,b,h);
            temp=NewBox;
            cout<<temp<<endl;
        }
        if(type==3)
        {
            int l,b,h;
            cin>>l>>b>>h;
            Box NewBox(l,b,h);
            if(NewBox<temp)
            {
                cout<<"Lesser"<<endl;
        }
            else
            {
                cout<<"Greater"<<endl;
            }
        }
        if(type==4)
        {
            cout<<temp.CalculateVolume()<<endl;
        }
        if(type==5)
        {
            Box NewBox(temp);
            cout<<NewBox<<endl;
        }
    }
}

int main()
{
    BoxesCreated = 0;
    BoxesDestroyed = 0;
    check2();
    cout<<"Boxes Created : "<<BoxesCreated<<endl<<"Boxes Destroyed : "<<BoxesDestroyed<<endl;
}
