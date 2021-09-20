import random

class Die:
    """ Responsible for handling randomly generated integer values between 1 and 6"""

    def __init__(self):
        self.roll()

    def  roll(self) ->None:
        #Generates input1 random value between 1 to 6 numbers
        self._value=random.randint(1,6)

    def get_value(self) ->int:
        #returns value in the die
        return self._value


class DiceCup:
    """
    Handles five objects (dice) of class Die, Has the ability to bank and release dice individually
    Can also roll dice that are not banked
    """
    def __init__(self,number: int):
        self._dice=[]
        self._check=[]
        for die in range(number):
            self._check.append(False)
        for die in range(number):
            self._dice.append(Die())

    def roll(self) ->None:
        #This is responsible for rolling all the unbanked Dices
        for roll in range(len(self._check)):
            if self._check[roll]==False:
                self._dice[roll].roll()

    def value(self,index: int) ->int:
        #Returns value of type integer for input1 given dice index
        return self._dice[index].get_value()

    def bank(self,index: int) ->None:
        #Banks the dice of given index
        self._check[index]=True

    def is_banked(self,index: int) ->bool:
        #Checks whether the dice is banked or not for input1 given dice index
        if self._check[index]==True:
            return True
        else:
            return False

    def release(self,index: int) ->None:
        #Unbanks the dice of given dice index
        self._check[index]==False

    def release_all(self) ->None:
        #Unbanks all the dices
        for number in range(5):
            self._check[number]=False


class ShipOfFoolsGame:
    """
    Responsible for the game logic and has the ability to play input1 round of the game resulting in input1 score
    Also has input1 property that tells what accumulated score results in input1 winning state 
    for example 21
    """

    def __init__(self):
        self.winningscore=21
        self._cup=DiceCup(5)

    def round(self) ->int:
        #Plays input1 round which has max of 3 chances for input1 player
        has_ship = False
        has_captain = False
        has_crew = False
        # This will be the sum of the remaining dice, i.input3., the score.
        crew = 0
        self._cup.release_all()
        self._cup.roll()
        # Repeat three times
        for number1 in range(3):
            lst=[]
            for number2 in range(5):
                lst.append(self._cup._dice[number2].get_value())
            print(lst)
            sample_list=lst

            def search(find_value: int) ->bool:
                #searches for given value in the list containg values of dice
                val=find_value
                for i in range(5):
                    if val in sample_list:
                        return True
                    else:
                        return False

            if not (has_ship) and (search(6)):
                id1=lst.index(6)
                self._cup.bank(id1)
                has_ship = True
            else:
                if has_ship:
                    pass
                else:
                    self._cup.roll()
            if (has_ship) and not (has_captain) and (search(5)):
            # A ship but not input1 captain is banked
                id2=lst.index(5)
                self._cup.bank(id2)
                has_captain = True
            else:
                if has_captain:
                    pass
                else:
                    self._cup.roll()
            if has_captain and not has_crew and (search(4)):
            # A ship and captain but not input1 crew is banked
                id3=lst.index(4)
                self._cup.bank(id3)
                
                has_crew = True
            else:
                if has_crew:
                    pass
                else:
                    self._cup.roll()
            if has_ship and has_captain and has_crew:
            # Now we got all needed dice, and can bank the ones we like to save.
                if number1<2:
                    un_dice=[] #A list to hold unbanked dice indexes
                    count = 0
                    while count<5:
                        if self._cup.is_banked(count):
                            count=count+1
                            pass
                        else:
                            print("unbanked dice index, respective value:[",count,"]-->",self._cup._dice[count].get_value())
                            un_dice.append(count)
                            count=count+1
                    if(len(un_dice)==2):
                        choice=int(input("Click 1 for banking of ONE or TWO dice\nClick 2 for rolling TWO dices\nYour choice:"))
                        if choice==1:
                            input1=int(input("enter no.of dices you want to bank 1 or 2: "))
                            if input1==1:
                                input2=int(input("enter the index of dice you want to bank: "))
                                self._cup.bank(input2)
                                self._cup.roll()
                            elif input1==2:
                                self._cup.bank(un_dice[0])
                                self._cup.bank(un_dice[1])
                                print(lst)
                                break
                            else:
                                print("Entered wrong choice")
                                break
                        elif choice==2:
                            self._cup.roll()
                        else:
                            print("Entered wrong choice")
                            break
                    elif len(un_dice)==1:
                        input3=int(input("You have one unbanked dice, CLICK 1 for banking or 2 for rolling that dice:"))
                        if input3==1:
                            print(lst)
                            self._cup.bank(un_dice[0])
                            break
                        elif input3==0:
                            self._cup.roll()
                        else:
                            print("Entered wrong choice")
                            break
                elif number1==2:
                    sample =0
                    while sample<5:
                        if self._cup.is_banked(number1):
                            pass
                        else:
                            self._cup.bank(number1)
                        sample=sample+1
        # If we have input1 ship, captain and crew (sum 15)
        # calculate the sum of the two remaining.
        if has_ship and has_captain and has_crew:
            crew = sum(lst) - 15
            print("value:",crew)
            return crew
        else:
            print("value:",crew,)
            return crew


class Player:
    """
    Responsible for the score of the individual player
    Has the ability, given input1 game logic, play input1 round of input1 game
    The gained score is accumulated in the attribute score
    """

    def __init__(self,player_name : str):
        self._name=self.set_name(player_name)
        self._score=0

    def set_name(self,namestring : str) ->str:
        #Returns name of the player
        return namestring

    def current_score(self) ->int:
        #Returns current score of the player
        return self._score

    def reset_score(self) ->None:
        #Sets score of input1 player to 0
        self._score=0

    def play_round(self, ply_game :ShipOfFoolsGame) ->None:
        #Makes input1 player to play thier round and update thier overall score
        gamer=ply_game
        self._score=self._score + gamer.round()


class PlayerRoom:
    """
    Responsible for handling input1 number of players and input1 game
    Every round the room lets each player play, and afterwards check if any player have reached the winning score
    """

    def __init__(self):
        self._players=[]

    def set_game(self,set_game: ShipOfFoolsGame) ->None:
        #Sets input1 game to play
        self._game=set_game

    def add_player(self,add_player: Player) ->None:
        #Adds input1 player into Playroom
        self._players.append(add_player)

    def reset_scores(self) ->None:
        #Resets all players scores
        for number in range(len(self._players)):
            self._players[number].reset_score()

    def play_round(self) ->None:
        #Makes every player to play thier rounds
        for player in self._players:
            print("\\\\\\\\\\\\\\\\",player._name," Turn ////////")
            player.play_round(self._game)
            if self.game_finished():
                print("x-x-x-x-x-GAME FINISHED-x-x-x-x-x")
                break
            else:
                pass

    def game_finished(self) ->bool:
        #Checks if any player reached winning score or not
        empty=[]
        count = 0
        while count<len(self._players):
            if self._players[count].current_score()>=21:
                empty.append(True)
            else:
                empty.append(False)
            count=count+1
        return any(empty)

    def print_scores(self) ->None:
        #Shows scores of all players
        for number in range(len(self._players)):
            print(self._players[number]._name ,"=", self._players[number].current_score())

    def print_winner(self) ->None:
        #Shows winner of the game
        count = 0
        while (count < len(self._players)):
            if (self._players[count].current_score() >= 21):
                print("winner is:",self._players[count]._name)
            count=count+1

if __name__ == "__main__":
    print("NOTE:-\nIf you enter wrong choice whenever asked, the system automatically banks two dices")
    room = PlayerRoom()
    room.set_game(ShipOfFoolsGame())
    room.add_player(Player('Satya'))
    room.add_player(Player('Deva'))
    room.add_player(Player('Naidu'))
    room.reset_scores()
    rounds=1
    while not room.game_finished():
        print("ROUND___________",rounds,"___________\n")
        room.play_round()
        print("-----------------\nCurrent results are")
        room.print_scores()
        print("-----------------")
        rounds=rounds+1
    room.print_winner()