//
//  ViewController.m
//  TextFormatter
//
//  Created by Haemanth S P on 17/05/16.
//  Copyright © 2016 Haemanth S P. All rights reserved.
//

#import "ViewController.h"

@interface ViewController ()
@property (weak, nonatomic) IBOutlet UITextView *textBody;

@end

@implementation ViewController

- (void)viewDidLoad {
  [super viewDidLoad];
  // Do any additional setup after loading the view, typically from a nib.
}

- (IBAction)setButtonBackgroundAsFontColor:(UIButton *)sender {
  [self.textBody.textStorage addAttribute:NSForegroundColorAttributeName value:sender.backgroundColor range:self.textBody.selectedRange];
}

@end
