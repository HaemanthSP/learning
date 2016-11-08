#include<iostream>

class person
{
  public:
  
  char n; 
  person()
  {
    n = 'a'; 
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
  public:
  char name;
  student(char a)
  { name = a;
    std::cout<< "Constructor - child" << std::endl;
  }
  student()
  { std::cout<< "Empty constructor - child" << std::endl;
  } 
  void disp()
  { std::cout<< name << std::endl;
  }
};

int main()
{ person* p = new student('b');
  student s('k');
  s.disp();
  p->disp();
}
