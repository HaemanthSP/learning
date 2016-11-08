#include <iostream>
#include <vector>
using namespace std;

int main()
{
  vector<vector<int> > inp; // GrayScale image.
  vector<vector<int> > win; // Convolution kernal.
  vector<vector<int> > out; // Result image (Not used currently).
  int N, M, data, con;
  int xU,yU, xL, yL, wxL, wyL ; // Offsetes. 
  
  // Read dimensions of image and window.
  cin >> N >> M;
  
  // Read image data.
  cout << "Enter the image data .." << endl;
  for(int i=0; i<N; i++)
  { vector<int> temp;
    for(int j=0; j<N; j++)
    {
      cin >> data;
      temp.push_back(data);
    }
    inp.push_back(temp);
    temp.clear();
  }
  
  // Read kernal window.
  cout << "Enter the window data .." << endl;
  for(int i=0; i<M; i++)
  { vector<int> temp;
    for(int j=0; j<M; j++)
    {
      cin >> data;
      temp.push_back(data);
    }
    win.push_back(temp);
    temp.clear();
  }

  // Slide the window across the image.
  for(int x=0; x<N; x++)
  { for(int y=0; y<N; y++)
    { 
      xU = x + int(M/2) + 1; 
      yU = y + int(M/2) + 1;
      xL = x - int(M/2);
      yL = y - int(M/2);
      wxL = 0;
      wyL = 0;

      // Edge case handling    
      if(x+int(M/2) >= N)
        xU = N; // Upper bound of x. 
      if(y+int(M/2) >= N)
        yU = N; // Upper bound of y.
      if(x-int(M/2) < 0)
      { xL = 0; // Lower bound of x.
        wxL = int(M/2) - x; // x Offset for window.
      } 
      if(y-int(M/2) < 0)
      { yL = 0; // Lower bound of y.
        wyL = int(M/2) - y; // y offset for window
      }

      con = 0;
      for(int i=xL; i<xU; i++)
        for(int j=yL; j<yU; j++)
          con += inp[i][j]* win[i-xL+wxL][j-yL+wyL];
      
      // Result   
      cout<< "X :" << x << "  Y :" << y << " == " << con << endl;
    }
  }
}   
