import random

class Die:
    '''  Die class manages the rolling of dice and getting values'''
    def __init__(self) -> None:
        self.roll()

    def roll(self) -> None:
        ''' def roll manages to roll the dice and stores the value in self._values'''
        self._value=random.randint(1,6)
    
    def get_value(self) -> int:
        '''def get_value manages to  get the values after rolling the dice'''
        return self._value

class Dicecup:
    '''Dicecups manages five dice of class Die,
       banks and releases dice individually'''

    def __init__(self, no_of_dices: int)-> None:

        self._no_of_dices = no_of_dices
        self._dices=[[0,Die()] for i in range(no_of_dices)]
    
    def value(self, index: int)-> int:
        '''def value manages to take index based value of dice'''

        return self._dices[index][1].get_value()
    
    def bank(self, index: int) -> None:
        '''def bank manages to hold a specific dice based on the index'''

        self._dices[index][0]=1

    def is_banked(self, index: int) -> bool:
        '''def is_banked manages the index position, if it is banked or not and the output is given in boolean value'''

        if self._dices[index][0]==1:
            return True
        else:
            return False
    
    def release(self, index: int) -> None:
        '''release  manages to release a specific indexed banked dice'''

        self._dices[index][0]=0

    def release_all(self) -> None:
        '''def release_all  manages to release all the banked dices'''

        for releasing_index in range(self._no_of_dices):
            self._dices[releasing_index][0]=0

    def roll(self) -> None:
        '''def roll manages to roll all unbanked dice '''

        count=0
        for rolling in self._dices:
            if rolling[0]==0:
                self._dices[count][1].roll()
            count=count+1

class ShipOfFoolsGame:
    '''ShipOfFoolsGame class is the original implementation of game which has a single method called round
          and responsible for the score of the players'''
    def __init__(self) -> None:

        self._cup=Dicecup(5)
        self._winning_score=21

    def round(self) -> int:
        '''def round manages to play player round which has max of 3 chances for player'''
        has_ship = False
        has_captain = False
        has_crew = False

        cargo_score = 0

        self._cup.release_all()

        for chance in range(3):
            self._cup.roll()
            '''Repeat three times'''
            dice_values=[self._cup._dices[i][1].get_value() for i in range(5)]
            print(dice_values)

            if not has_ship and dice_values.count(6):
                """If has no ship and found 6 bank respective dice"""
                self._cup.bank(dice_values.index(6))
                has_ship = True
            
            if has_ship and not has_captain and dice_values.count(5):
                '''A ship but not a captain is banked'''
                self._cup.bank(dice_values.index(5))
                has_captain = True
            
            if has_captain and not has_crew and dice_values.count(4):
                '''A ship and captain but not a crew is banked'''
                self._cup.bank(dice_values.index(4))
                has_crew = True
            
            if has_captain and has_crew and has_ship:
                '''Now we got all needed dice, and can bank the dices 
                with value greater than 3 or else roll the unbanked dices'''
                if chance<2:
                    for check in range(5):
                        if self._cup._dices[check][1].get_value() > 3 and not self._cup.is_banked(check):
                            self._cup.bank(check)
                            print("Banked",self._cup._dices[check][1].get_value(),"of die number",check+1)
                if chance==2:
                    for check in range(5):
                        if self._cup.is_banked(check):
                            pass
                        else:
                            self._cup.bank(check)
                            '''If we have a ship, captain and crew (sum 15), 
                               calculate the sum of the two remaining'''
                            
        if has_captain and has_crew and has_ship:
            for sum in range(5):
                cargo_score = cargo_score+self._cup._dices[sum][1].get_value()
            cargo_score=cargo_score-15
            print("Cargo score is",cargo_score)
        else:
            print("Cargo score is",cargo_score)
        
        return cargo_score

class Player:
    '''player class manages the individual player and manages the score of the  
    individual player and stores the score in the ._player_score attribute'''
    
    def __init__(self, name_of_player : str) -> None:
        self._player_name = self.set_name(name_of_player)
        self._player_score = 0
    
    def set_name(self, namestring: str) -> str:
        '''def set_name manages to set the name the player'''
        return namestring

    def current_score(self) -> int:
        '''def current_score returns the score of the player'''
        return self._player_score

    def reset_score(self) -> None:
        '''def reset_score manages to reset the score of the player'''
        self._player_score = 0
    
    def play_round(self, game) -> None:
        '''def play_round manages to make use of ShipOfFoolsGame object and updates thier overall score'''
        self._player_score = self._player_score + game.round()
    
class PlayRoom:
    '''Playroom class manages to handle the players and checks the score and displays the winner'''
    
    def __init__(self) -> None:
        self._game = ShipOfFoolsGame()
        self._players = []
    
    def add_player(self, player: Player) -> None:
        '''def add_player manages to add the players to the game'''
        self._players.append(player)
    
    def reset_scores(self) -> None:
        '''def reset_score manages to reset all players scores'''
        for reset in self._players:
            reset.reset_score()
    
    def play_round(self) -> None:
        '''def play_round manages to make every player to play thier rounds'''
        for play in self._players:
            print("---------",play._player_name,"---------")
            play.play_round(self._game)
    
    def game_finished(self) -> bool:
        '''def game_finished manages to check if any player reached winning score or not'''
        for finish in self._players:
            if finish.current_score() >= 21:
                return True
        return False

    def print_scores(self) -> None:
        '''def print_score manages to show the current score of the each player'''
        for scores in self._players:
            print(scores._player_name,"is",scores.current_score())
    
    def print_winner(self) -> None:
        '''def print_winner shows the winner of the game
            If both players manage to cross winning score at same round then it is considered as draw
        '''
        count = 0
        for winner in self._players:
            if winner.current_score() >= 21:
                count=count+1
        if count>1:
            print("\n~~~~~~~~~~Draw~~~~~~~~~~~~")
        elif count == 1:
            for winner in self._players:
                if winner.current_score() >= 21:
                    print("\nHurray, the winner is",winner._player_name)

if __name__ == "__main__":
    room=PlayRoom()
    room.add_player(Player("Satya")) #adding player 1
    room.add_player(Player("Sri")) #adding player 2
    room.reset_scores()
    round_count = 1
    
    while not room.game_finished():
        print("\n***********_Round",round_count,"Begins")
        room.play_round()
        print("___________________________")
        room.print_scores()
        print("___________________________")
        round_count = round_count + 1
        
    room.print_winner()
    print("-----------------------------------")
    print(" Congrats, the game is finished :)")
    print("```````````````````````````````````")
