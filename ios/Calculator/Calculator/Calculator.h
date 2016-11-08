#import <Foundation/Foundation.h>

@interface Calculator : NSObject

@property (nonatomic) NSInteger result;

- (void)perform:(char)operation
          onOperand1:(NSInteger)operand1
         andOperand2:(NSInteger)operand2;
- (void)display;
@end