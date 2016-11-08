#include<iostream>

using namespace std;

int callA=0;
int callB=0;
int callC=0;
class A
{
protected:
   
   void func(int  & a)
   {
      a=a*2;
      callA++;
   }
};

class B
{
protected:
   void func(int & a)
   {
      a=a*3;
      callB++;
   }
};

class C
{
protected:
   void func(int & a)
   {
      a=a*5;
      callC++;
   }
};

class D : public A, public B, public C 
{

  int val;
  public:
  //Initially val is 1
  D()
  {
    val=1;
  }
  
  int quotient(int divident, int divisor)
  { int q = 0;
    while(divident%divisor == 0)
    { q++;
      divident /= divisor; 
    }
    return q;
  } 

  //Implement this function
  void update_val(int new_val)
  {
    int t2=0, t3=0, t5=0; 
    
    t2 = quotient(new_val, 2);
    t3 = quotient(new_val, 3);
    t5 = quotient(new_val, 5);
   
    cout << t2 << " " << t3 << " " << t5 << endl;
     
    for(int i=0; i<t2; i++)
      A::func(val);
    for(int i=0; i<t3; i++)
      B::func(val);
    for(int i=0; i<t5; i++)
      C::func(val);

   }

  //For Checking Purpose
   void check(int); //Do not delete this line.
};

void D::check(int new_val)
{
  update_val(new_val);
  cout<<"Value = "<<val<<endl<<"A's func called "<<callA<<" times "<<endl<<"B's func called "<<callB<<" times "<<endl<<"C's func called "<<callC<<" times"<<endl;
}

int main()
{
  D d;
  int new_val;
  cin>>new_val;
  d.check(new_val);
}


