#include<iostream>
#include<cmath>

class u_point
{
  public:
    int x;
    int y;
  u_point()
  {
  }
  u_point(int a, int b)
  {
    x = a; y = b;
  }
};

class u_vector
{
  public:
    u_point p1;
    u_point p2;
    
    u_vector(u_point a, u_point b)
    { 
      p1 = a;
      p2 = b;
    }
    float mag()
    { float x_diff = p1.x - p2.x;
      float y_diff = p1.y - p2.y;
      return sqrt(pow(x_diff, 2) + pow(y_diff, 2));
    }
    float phase()
    { 
      float x_diff = p1.x - p2.x;
      float y_diff = p1.y - p2.y;
      return atan(y_diff/x_diff);
    } 
};

int main()
{
  u_point a(1,2),b(2,3);
  u_vector v1(a,b);
  std::cout << "Magnitude of the vector : "  <<v1.mag() << std::endl;
  std::cout << "Angle of the vector : " <<v1.phase() << std::endl;
}
