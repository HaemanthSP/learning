#include<iostream>
#include<vector>

int main()
{
 int N, Q, k, ele;
 std::vector<std::vector<int> > data;

 std::cin >> N >> Q;

 for(int i=0; i<N ; i++)
 { std::cin >> k;
   std::vector<int> temp_data;
   for(int j=0; j<k; j++)
   { std::cin >> ele;
     temp_data.push_back(ele);
   }
   data.push_back(temp_data);
 }

 int x, y;
 for(int i=0; i<Q; i++)
 { std::cin >> x >> y;
   std::cout << data[x][y] << std::endl;
 }
}
