#include<iostream>

class employee
{
  public:
  void lunch_status()
  {
    std::cout<<"Available for Lunch";
  }
  void get_salary()
  {
    std::cout<< "salary updated";
  }
};

class project_engineer : public employee
{
  public:
  void learn()
  {
    std::cout<< "Doing my learning" << std::endl;
  }
};

class project_lead : public project_engineer
{ 
  public:
  void manage()
  {
    std::cout<< "Handling Projects" << std::endl;
  }
};

int main()
{
  project_lead pl;
  pl.manage();
}
