#include<iostream>
#include<string>
#include<vector>
int field; 
bool isLarger(std::vector<int> x, std::vector<int> y) 
{
  return x[field] > y[field];
}

class gf_list
{
  
  public:
    std::string name;
    std::vector<std::vector<int> > details;
   
    void sort_gf(int i)
    {
      field = i;
      sort(details.begin(), details.end(), isLarger);
      disp();
    }
   
    void disp()
    {
      if(!details.empty())
      { 
        std::cout << details.size() << " * " << details[0].size() << std::endl;
        for(int i = 0; i < details.size(); i++)
        {
          for(int j = 0; j< details[0].size(); j++)
            std::cout << details[i][j] << "\t";
          std::cout<<"\n";
        }
      }
    }
};

int main()
{
  int i = 0;
  int data;
  char opt;
  gf_list list1;
  while(1)
  { std::vector<int> temp;
    i++;
    std::cout << "Enter Girl Friend Deatails..";
    std::cout << "\nAge ..:";
    std::cin >> data;
    temp.push_back(data);
    std::cout << "\nHeight ..:";
    std::cin >> data;
    temp.push_back(data);
    std::cout << "\nWeight ..:";
    std::cin >> data;
    temp.push_back(data);
    list1.details.push_back(temp);
    temp.clear();
    std::cout << "\nEnter more .(y/n) :";
    std::cin >> opt;
    if(opt == 'n' | opt == 'N')
      break;
  }

   list1.disp();
   std::cout << "Sort array based on\n1.Age\n2.Height\n3.Weight" <<std::endl; 
   std::cin >> data;
   list1.sort_gf(data-1); 
}
