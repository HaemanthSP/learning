#import <Foundation/Foundation.h>
#import "Deck.h"

@interface CardMatchGame : NSObject

// desgnated initializer
- (instancetype)initWithCount:(NSUInteger)count
                    usingDeck:(Deck *)deck;
- (void)chooseCardAtIndex:(NSUInteger)index;
- (Card *)cardAtIndex:(NSUInteger)index;

@property (nonatomic , readonly) NSInteger score;

@end