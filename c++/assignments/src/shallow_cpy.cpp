#include<iostream>
#include <opencv2/opencv.hpp>

int main()
{ 
  float data[10] = {1,2,3,4,5,7,8,9,10};
  cv::Mat a(1,10, CV_32FC1, &data);
  cv::Mat b = a;
  b.at<float>(0) = 32;
  std::cout << "Duplicate" << b << std::endl;
  std::cout << "original" << a <<  std::endl;
}
