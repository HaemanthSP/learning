//
//  ViewController.m
//  cardExample
//
//  Created by Haemanth S P on 09/05/16.
//  Copyright © 2016 Haemanth S P. All rights reserved.
//

#import "ViewController.h"
#import "PlayingDeck.h"
#import "CardMatchGame.h"

@interface ViewController ()
@property (weak, nonatomic) IBOutlet UILabel *flipLable;
@property (nonatomic) int flipCount;
@property (strong, nonatomic) Deck* deck;
@property (strong, nonatomic) CardMatchGame * game;
@property (strong, nonatomic) IBOutletCollection(UIButton) NSArray *cardButtons;
@property (weak, nonatomic) IBOutlet UILabel *scoreLabel;
@end

@implementation ViewController

- (CardMatchGame *)game
{
  if (!_game) _game = [[CardMatchGame alloc] initWithCount:[self.cardButtons count]usingDeck:[self createDeck]];
  return _game;
}


- (Deck *) deck
{
  if(! _deck) _deck = [self createDeck];
  return _deck;
}

- (Deck *) createDeck
{
  return [[PlayingDeck alloc]init];
}

- (void)viewDidLoad {
  [super viewDidLoad];
  // Do any additional setup after loading the view, typically from a nib.
}

- (void)didReceiveMemoryWarning
{
  [super didReceiveMemoryWarning];
  // Dispose of any resources that can be recreated.
}


- (IBAction)touchCard:(UIButton *)sender
{
  int choosenButtonIndex = [self.cardButtons indexOfObject:sender];
  [self.game chooseCardAtIndex:choosenButtonIndex];
  [self updateUI];
  self.flipCount++;
}

- (void) updateUI
{
  for (UIButton *cardButton in self.cardButtons) {
    int cardButtonIndex = [self.cardButtons indexOfObject:cardButton];
    Card *card = [self.game cardAtIndex:cardButtonIndex];
    [cardButton setTitle:[self titleForCard:card] forState:UIControlStateNormal];
    [cardButton setBackgroundImage:[self backgroundImageForCard:card] forState:UIControlStateNormal];
    cardButton.hidden = card.isMatched;
    self.scoreLabel.text = [NSString stringWithFormat:@"Score : %d", self.game.score];
  }
}


- (NSString* )titleForCard:(Card *)card
{
  return card.isChosen ? card.content : @"" ;
}

- (UIImage *)backgroundImageForCard:(Card *)card
{
  return [UIImage imageNamed:card.isChosen ? @"cardFront" : @"cardBack"];
}
/*- (IBAction)touchCard:(UIButton *)sender
{
  if ([sender.currentTitle length]) {
    
    [sender setBackgroundImage:[UIImage imageNamed:@"cardBack"]
                      forState:UIControlStateNormal];
    [sender setTitle:@"" forState:UIControlStateNormal];
  } else
  {
    Card *card = [self.deck drawRandomCard];
    if(card)
    {
    [sender setBackgroundImage:[UIImage imageNamed:@"cardFront"]
                      forState:UIControlStateNormal];
    [sender setTitle:card.content forState:UIControlStateNormal];
    self.flipCount++;
    }
   
  }
}
*/

- (void) setFlipCount:(int) flipCount
{
  _flipCount = flipCount;
  self.flipLable.text = [NSString stringWithFormat:@"Flips: %d", self.flipCount];
}
@end
