//
//  ViewController.m
//  HelloWorld
//
//  Created by Haemanth S P on 05/05/16.
//  Copyright © 2016 Haemanth S P. All rights reserved.
//

#import "ViewController.h"

@interface ViewController ()

@end

@implementation ViewController

- (void)viewDidLoad {
  [super viewDidLoad];
  self.view.backgroundColor = [UIColor greenColor];

  
  
  // Do any additional setup after loading the view, typically from a nib.
}

- (void)didReceiveMemoryWarning {
  [super didReceiveMemoryWarning];
  // Dispose of any resources that can be recreated.
}

- (void) loadView
{
   CGRect viewRect = [[UIScreen mainScreen]  bounds];
   UIView *colorView = [[UIView alloc] initWithFrame:viewRect];
   self.view = colorView;
}

- (void)touchesBegan:(NSSet<UITouch *> *)touches withEvent:(UIEvent *)event
{
  self.view.backgroundColor = [UIColor yellowColor];
}

- (void)touchesEnded:(NSSet<UITouch *> *)touches withEvent:(UIEvent *)event
{
  self.view.backgroundColor = [UIColor blueColor];
}
@end
