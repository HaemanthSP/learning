#import "Calculator.h"

@interface Calculator()

@end

@implementation Calculator

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

- (void)display
{
  NSLog(@"Dispaly is accessed");
}

@end