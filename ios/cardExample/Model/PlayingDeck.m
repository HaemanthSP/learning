#import "PlayingDeck.h"

@interface PlayingDeck()
@end


@implementation PlayingDeck

- (instancetype)init
{
  self = [super init];
  if (self) {
     for (NSString *suit in [PlayingCard validSuits]) {
      for (NSUInteger rank=1; rank<=[PlayingCard maxRank]; rank++) {
        PlayingCard *card = [[PlayingCard alloc] init];
        card.rank = rank;
        card.suit = suit;
        [self addCard:card atTop:false];
      }
    }
  }
  return self;
}

@end