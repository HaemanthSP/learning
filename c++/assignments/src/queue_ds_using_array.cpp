#include<iostream>
#include<cstdlib>

class queue_ds
{
  public:
  int q[10];
  int rear;

  queue_ds()
  { 
    rear = -1;
  }
  void insert_ele(int x)
  { 
    if(rear >= 9)
    { std::cout << "Queue limit exceeded" << std::endl;
    }
    else
    { rear++;
      q[rear] = x;
      std::cout << "Element inserted" << std::endl;
    }
  }

  void delete_ele()
  { 
    if(rear == -1)
    { std::cout << "Queue is empty" << std::endl;
    }
    else
    {
      for(int i = 0; i < rear; i++)
      { q[i] = q[i+1];
      }
      rear--;
      std::cout << "Deleted the first element" << std::endl;
    }
  }
  
  void display()
  {
    if(rear == -1)
    { std::cout << "Queue is empty" << std::endl;
    }
    else if(rear >= 9)
    { std::cout << "Queue limit exceeded" << std::endl;
    }
    else
    { 
      std::cout << "Queue : " << std::endl;
      for(int i = 0; i <= rear; i++)
      { std::cout << q[i] << "   ";
      }
    }
  }
};

int main()
{ queue_ds q1;
  char ch, w;
  int ele;
  bool abort = false;
  while(1)
  { 
    std::cout << "\n\nOptions :\n  1.Insert\n  2.Delete\n  3.Exit\n\n";
    std::cout << "Enter your choice ..." << std::endl;
    ch = getchar();
    switch(ch)
    {
      case '1':
      { std::system("clear");
        std::cout << "Enter the number" << std::endl;
        std::cin >> ele;
        q1.insert_ele(ele);
        std::system("clear");
        q1.display();
        w =  getchar();
        break;
      }
      case '2':
      { q1.delete_ele();
        std::system("clear");
        q1.display();
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
