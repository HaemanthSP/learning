#include<iostream>


int main()
{
 int N, Q, k, ele, MN = 0, MO = 0;

 std::cin >> N >> Q;
 long int* data;
 int* seq_lens = new int [N];
 for(int i=0; i<N ; i++)
 { std::cin >> k;
   *(seq_lens+i) = seq_lens[i-1]+k;
   MO = MN;
   MN = MO + k;
   long int* temp = new long int[MN];
   std::copy(data, data+MO, temp);
   for(int j=MO; j<MN; j++)
   { std::cin >> ele;
     *(temp+j) = ele;
   }  
   //delete[] data;
   data = temp;
 }
 for(int i=0; i<N; i++)
   std::cout << seq_lens[i] << '\t';
 int x, y;
 for(int i=0; i<Q; i++)
 { std::cin >> x >> y;
   std::cout << "index" <<seq_lens[x-1]+y << std::endl;
   std::cout << data[seq_lens[x-1]+y] << std::endl;
 }
 
}

// Solution found in hacker rank discussion
/*int n,q;
cin>>n>>q;
int** seq=new int* [n];
for(int i=0;i<n;i++)
    {
      int a;
      cin>>a;
      int* b=new int [a];
      for(int j=0;j<a;j++)
        {
          int e;
          cin>>e;
          b[j]=e;
        }
    *(seq+i)=b;
   }

  for(int i=0;i<q;i++)
  {
  int r,s;
  cin>>r>>s;
  cout<<seq[r][s]<<endl;
  }
*/
