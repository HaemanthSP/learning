#import "PlayingCard.h"

@implementation PlayingCard

@synthesize suit = _suit;


- (int) match:(NSArray *)otherCards
{
  int score = 0;
  if ([otherCards count] == 1) {
    PlayingCard *otherCard = [otherCards firstObject];
    if (otherCard.rank == self.rank) {
      score = 4;
    } else if ([otherCard.suit isEqualToString:self.suit]){
        score = 1;
    }
  }
  return score;
}

- (NSString *) content
{
  NSArray *rankString = [PlayingCard rankString];
  return [rankString[self.rank] stringByAppendingString:self.suit];
}

+ (NSArray *) validSuits
{
  return @[@"♠︎",@"♣︎",@"♥︎",@"♦︎"];
}

- (void)setSuit:(NSString *)suit
{
  if ([[PlayingCard validSuits] containsObject:suit]) {
    _suit = suit;
  }
}

+ (NSArray *) rankString
{
  return @[@"?",@"A",@"2",@"3",@"4",@"5",@"6",@"7",@"8",@"9",@"10",@"J",@"Q",@"K"];
}

+ (NSUInteger) maxRank {
  return [[self rankString] count]-1;
}


- (void) setRank:(NSUInteger)rank
{
  if (rank <= [PlayingCard maxRank]) {
    _rank = rank;
  }
}

- (NSString *) suit
{
  return _suit ? _suit : @"?";
}
@end
