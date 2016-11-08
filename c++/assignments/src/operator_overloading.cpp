#include<iostream>

class feature
{
 public:
 int a[5];

 feature()
 {
 }
 feature(int b)
 { a[0] = b[0];
   a[1] = b[1];
   a[2] = b[2];
   a[3] = b[3];
   a[4] = b[4];
 }
 
 feature operator +(feature f1,feature f2)
 {
  feature f3; 
  f3.a[0] = f1.a[0] + f2.a[0];  
  f3.a[1] = f1.a[1] + f2.a[1];  
  f3.a[2] = f1.a[2] + f2.a[2];  
 }
 
 void display()
 {
  std::cout << a;
 }

};

int main()
{
 int x[] = {1, 2, 3, 4, 5}, y[] = {2, 3, 4, 5, 6};
 feature a(x), b(y), c; 
 c = a + b;
 c.display();
}
