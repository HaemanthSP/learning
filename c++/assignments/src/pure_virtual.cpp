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
 public:
 char name;
 student(char a)
 {
  name = a;
 }
 student()
 { std::cout<< "Empty constructor - child" << std::endl;
 } 
 void disp()
 {
  std::cout<< "name" << std::endl;
 }
 
};

class student2 : public person
{
 public:
 char name;
 student2(char a)
 {
  name = a;
 }
 student2()
 { std::cout<< "Empty constructor - child" << std::endl;
 } 
 
};

int main()
{
  person* p = new student;
  student s('k');
  student2 s2;
  //s.disp();
  //p->disp();
}
