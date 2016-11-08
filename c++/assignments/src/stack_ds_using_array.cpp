#include<iostream>
#include<cstdlib>

class stack_ds
{
  public:
  int s[10];
  int rear;

  stack_ds()
  { 
    rear = -1;
  }
  void insert_ele(int x)
  { 
    if(rear >= 9)
    { std::cout << "Stack Overflow" << std::endl;
    }
    else
    { rear++;
      s[rear] = x;
      std::cout << "Element inserted" << std::endl;
    }
  }

  void delete_ele()
  { 
    if(rear == -1)
    { std::cout << "Stack is empty" << std::endl;
    }
    else
    { rear--;
      std::cout << "Deleted the first element" << std::endl;
    }
  }
  
  void display()
  { 
    if(rear == -1)
    { std::cout << "Stack is empty" << std::endl;
    }
    else if(rear >= 9)
    { std::cout << "Stack Overflow" << std::endl;
    }
    else
    { 
      std::cout << "Stack : " << std::endl;
      for(int i = rear; i >= 0; i--)
      { std::cout << s[i] << '\n';
      }
    }
  }
};

int main()
{ stack_ds s1;
  char ch, w;
  int ele;
  bool abort = false;
  while(1)
  { 
    std::cout << "\n\nOptions :\n  1.Insert\n  2.Delete\n  3.Exit\n\nEnter your choice ..." << std::endl;
    ch = getchar();
    switch(ch)
    {
      case '1':
      { std::system("clear");
        std::cout << "Enter the number" << std::endl;
        std::cin >> ele;
        s1.insert_ele(ele);
        std::system("clear");
        s1.display();
        w =  getchar();
        break;
      }
      case '2':
      { s1.delete_ele();
        std::system("clear");
        s1.display();
        w = getchar();
        break;
      }
      case '3':
      { abort = true;
        break;
      }
      default:
      { std::cout << "Invalid selection" << std::endl;
        std::system("clear");
      }
    }
    if(abort)
      break; 
  } 
}
