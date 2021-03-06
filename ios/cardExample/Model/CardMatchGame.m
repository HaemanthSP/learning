#import "CardMatchGame.h"

@interface CardMatchGame()

@property (nonatomic, readwrite) NSInteger score;
@property (strong, nonatomic) NSMutableArray* cards; // of Card
@end

@implementation CardMatchGame

- (NSMutableArray *)cards
{
  if (!_cards) _cards = [[NSMutableArray alloc] init];
  return _cards;
}

- (instancetype)initWithCount:(NSUInteger)count usingDeck:(Deck *)deck
{
  self = [super init];
  
  if (self) {
    for (int i=0; i<count; i++) {
      Card *card = [deck drawRandomCard];
      if (card) {
        [self.cards addObject:card];
      }
      else
      {
        self = nil;
        break;
      }
    }
  }
  return self;
}

static const int BONUS = 4;
static const int PENALTY = 2;
static const int COST_TO_CHOOSE = 1;

- (void)chooseCardAtIndex:(NSUInteger)index
{
  Card *card = [self cardAtIndex:index];
  if(!card.isMatched)
  {
    if (card.isChosen) {
      card.chosen = NO;
    } else {
      for (Card *otherCard in self.cards) {
        if (otherCard.isChosen && !otherCard.isMatched) {
          int matchScore = [card match:@[otherCard]];
          if (matchScore) {
            self.score += matchScore * BONUS;
            otherCard.matched = YES;
            card.matched = YES;
          } else {
            self.score -= PENALTY ;
            otherCard.chosen = NO;
          }
          break;
        }
      }
      self.score -= COST_TO_CHOOSE;
      card.chosen = YES;
    }
  }
  
}

-(Card *)cardAtIndex:(NSUInteger)index
{
  return (index <  [self.cards count]) ? self.cards[index] : nil;
}

- (instancetype) init
{
  return nil;
}

@end


