//
//  ViewController.m
//  Calculator
//
//  Created by Haemanth S P on 12/05/16.
//  Copyright © 2016 Haemanth S P. All rights reserved.
//

#import "ViewController.h"

@interface ViewController ()

@property (strong, nonatomic) Calculator *calc;
@property (weak, nonatomic) IBOutlet UILabel *dispMain;
@property (weak, nonatomic) IBOutlet UILabel *dispSub;
@property (strong, nonatomic) IBOutletCollection(UIButton) NSArray *operatorKeyPad;
@property (strong, nonatomic) IBOutletCollection(UIButton) NSArray *numKeyPad;
@property (strong, nonatomic) NSString *dispText;
@property (strong, nonatomic) NSString *dispSubText;
@property (nonatomic) NSInteger operand1;
@property (nonatomic) NSInteger operand2;
@property (nonatomic) char operation;
@property (nonatomic) NSInteger result;
@property (nonatomic) BOOL isLastOperator;

@end

@implementation ViewController

- (void) setCalc:(Calculator *)calc
{
  if (!_calc) _calc = [[Calculator alloc] init];
  _calc = calc;
  [_calc display];
}

- (void) setDispText:(NSString *)dispText
{
  _dispText = dispText;
  [_calc display];
  self.dispMain.text = self.dispText;
}

- (NSString *) getDispText:(NSString **)buffer range:(NSRange)inRange
{
  if (_dispText == nil) _dispText = @"0";
  return _dispText;
}

- (void) setDispSubText:(NSString *)dispSubText
{
  _dispSubText = dispSubText;
  self.dispSub.text = self.dispSubText;
}


- (IBAction)enteredNumber:(UIButton *)sender
{
  if (self.dispText == NULL) {
    self.dispText = @"";
  }
  
  self.dispText = [self.dispText stringByAppendingString:[NSString stringWithFormat:@"%ld",[self.numKeyPad indexOfObject:sender]]];
  self.isLastOperator = false;
}

- (IBAction)enteredOpration:(UIButton *)sender
{
  char operations[] = {'+','-','*','/'};
  NSUInteger operatorIndex = [self.operatorKeyPad indexOfObject:sender];
  
  
  if (operatorIndex == 5)
  {
  self.dispSubText = [self.dispSubText stringByAppendingString:self.dispText];
  self.operand2 = [[self.dispText substringWithRange:NSMakeRange(1, [self.dispText length]-1)] integerValue];
  self.isLastOperator = false;
  //self.operand2 = 2;
  NSLog(@"%@",[self.dispText substringWithRange:NSMakeRange(1, [self.dispText length]-1)]);
  NSLog(@"%ld %c %ld",self.operand1, self.operation, self.operand2);

  [self perform:self.operation onOperand1:self.operand1 andOperand2:self.operand2];
   self.operand1 = self.result;
   self.dispText = [NSString stringWithFormat:@"%ld", (long)self.result];
   self.isLastOperator = true;
  }
  else if (operatorIndex == 4)
  {
    if ([self.dispText length] > 1)
      self.dispText = [self.dispText substringToIndex:[self.dispText length]-1];
    else
      self.dispText = @"";
  }
  else
  {
    //if (!self.isLastOperator) {
      self.operand1 = [self.dispText integerValue];
      self.dispSubText = self.dispText;
    //  self.isLastOperator = true;
    //}
    
    self.operation = operations[operatorIndex];
    self.dispText = [NSString stringWithFormat:@"%c",self.operation];
  }
  
}

- (void)perform:(char)operation onOperand1:(NSInteger)operand1 andOperand2:(NSInteger)operand2
{
  NSLog(@"Enters calculator...");
  switch (operation) {
    case '+':
      self.result =  operand1 + operand2;
      break;
    case '-':
      self.result = operand1 - operand2;
      break;
    case '*':
      self.result = operand1 * operand2;
      break;
    case '/':
      self.result = operand1 / operand2;
      break;
      
    default:
      self.result = -1;
      break;
  }
}


@end
