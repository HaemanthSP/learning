#include<iostream>

class person
{
  public:
  person()
  { 
    std::cout<< "Empty constructor - parent" << std::endl;
  }
  
  virtual void disp()=0;
  /*virtual void disp()
  {
   std::cout << "parent" << std::endl;
  }
  */
};

class student : public person
{ 
  student(char a)
  { name = a;
  }
  public:
  char name;
  student()
  { std::cout<< "Empty constructor - child" << std::endl;
  } 
  void disp()
  { std::cout<< "name" << std::endl;
  }
};

int main()
{ person* p = new student;
  student s('k');
  s.disp();
  p->disp();
}
