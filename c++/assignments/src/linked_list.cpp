#include<iostream>
#include<cstdlib>

class Node 
{
  public:

  int val;
  Node* next;

  Node()
  {
    std::cout << "Default Constructor" << std::endl;
    next = NULL;
  }

  Node(int v)
  {
    val = v;
    next = NULL;
  }
};

static Node* head = NULL;
static Node* tail = NULL;

class Linked_list
{
  public:
   
  Linked_list()
  {
  }

  void insert_beg(int n_val)
  { 
    Node *new_node = new Node;
    Node *temp;
    temp = head;
    head = new_node;
    new_node -> val = n_val;
    new_node -> next = temp;
  }
 
  void insert_end(int n_val)
  { 
    Node *new_node = new Node;
    new_node->val = n_val;
    if(head == NULL)
    {
      std::cout<< "First ELEMENT" << std::endl;
      head = new_node;
      tail = head;
    }
    else 
    { if(tail == NULL)
      { head->next = new_node;
        tail = head;
      }
      else
      {
      tail = tail->next;
      tail->next = new_node;
      }
    }
  }
  
  void del_beg()
  {
   head = head->next; 
  }

  void del_end()
  {
   tail->next = NULL;
  }
  void display()
  {
    std::cout << "Entering display" << std::endl; 
    Node* temp = head;
    while(1)
    { 
      std::cout << temp->val << std::endl; 
      if(temp->next == NULL)
        break;
      temp = temp->next;
    }
  }
};

int main()
{ Linked_list l1;
  bool abort = false;
  while(1)
  {
   int opt, data;
   std::cout << "Options ...\n";
   std::cout << "1.Insert at the begining\n";
   std::cout << "2.Insert at the end\n";
   std::cout << "3.Delete at the begining\n";
   std::cout << "4.Delete at the end\n";
   std::cout << "5.Exit\n";
   std::cout << "Enter your choice ..";
   std::cin >> opt;
   switch(opt)
   {
     case 1: 
     { std::cout << "Enter the element.."; 
       std::cin >> data;
       l1.insert_beg(data);
       std::system("clear"); 
       l1.display();
       break;
     }
     case 2: 
     { std::cout << "Enter the element.."; 
       std::cin >> data;
       l1.insert_end(data);
       std::system("clear"); 
       l1.display();
       break;
     }
     case 3: 
     {
       l1.del_beg();
       std::system("clear"); 
       l1.display();
       break;
     }
     case 4: 
     { 
       l1.del_end();
       std::system("clear"); 
       l1.display();
       break;
     }
     case 5:
     { abort = true; 
     }
     default:
     {
       std::cout << "Invalid Option ..";
       l1.display();
       std::system("clear");
     }
    }
    if(abort)
      break;
  }
}
