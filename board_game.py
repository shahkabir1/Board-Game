"""A code file simulating a Board game.
"""
import random
from time import sleep

d = [1, 2, 3, 4, 5, 6]


class Player:
    """A player in the board game.

    Attributes:
    - name: the name of the player.
    - position: the current position of the player.
    - turn_count: the number of turns this player has had.
    - win_count: the number of wins this player has had.
    - is_winner: indicates whether the player is the winner of the current game.
    - skip_turn: indicates whether the player's next turn should be skipped.

    Sample Usage:

    Creating a player:
    >>> p = Player('Shah')
    >>> p.position
    0
    >>> p.name
    'Shah'
    """
    # Attribute types
    name: str
    position: int
    turn_count: int
    win_count: int
    is_winner: bool
    skip_turn: bool

    def __init__(self, player_name: str) -> None:
        """Initialize a player.

        >>> p = Player('Shah')
        >>> p.position
        0
        >>> p.name
        'Shah'
        """
        self.name = player_name
        self.position = 0
        self.turn_count = 0
        self.win_count = 0
        self.is_winner = False
        self.skip_turn = False


class Board:
    """A board for the game.

    Attributes:
    - players: a list of players in the game.
    - spaces: the number of spaces on the board.
    - winner_record: the record of winners in the game.
    - licorice_spaces: the positions on the board which will cause
    a player's turn to be skipped.
    - turn_record: a record of the names of each turn.
    - games_played: the number of games played on this board.
    - winner: determines if the current game has a winner or not.


    Representation Invariants:
    - len(players) == 2

    Sample Usage:

    Creating a board:
    >>> b = Board()
    >>> b.licorice_spaces
    [10, 20, 30, 40, 50, 60, 70, 80, 90]
    >>> b.players
    []
    >>> b.spaces
    100
    >>> b.winner_record
    []
    """

    def __init__(self) -> None:
        """Initialize a game board.

        >>> b = Board()
        >>> b.licorice_spaces
        [10, 20, 30, 40, 50, 60, 70, 80, 90]
        >>> b.players
        []
        >>> b.spaces
        100
        >>> b.winner_record
        []
        """
        self.players = []
        self.spaces = 100
        self.winner_record = []
        self.licorice_spaces = [10, 20, 30, 40, 50, 60, 70, 80, 90]
        self.turn_record = []
        self.games_played = 0
        self.winner = False
        self.game_start()

    def move(self, current_player: str) -> None:
        """Move the player forward, according to the role of a die."""
        roll = random.choice(d)
        for i in range(len(self.players)):
            if (self.players[i].name == current_player
                    and self.players[i].position + roll <= 100):
                if self.players[i].position not in self.licorice_spaces:
                    if len(self.turn_record) != 0:
                        if self.turn_record[-1] != current_player:
                            self.players[i].position += roll
                            self.turn_record.append(current_player)
                            sleep(0.5)
                            print(str(self.players[i].name)
                                  + "'s current position is "
                                  + str(self.players[i].position)
                                  + ".")
                        else:
                            if (self.players[0].position in self.licorice_spaces
                                    and self.players[0].name != current_player):
                                self.players[i].position += roll
                                self.turn_record.append(current_player)
                                sleep(0.5)
                                print(str(self.players[i].name)
                                      + "'s current position is "
                                      + str(self.players[i].position)
                                      + ".")
                            elif (self.players[1].position in
                                  self.licorice_spaces
                                  and self.players[1].name != current_player):
                                self.players[i].position += roll
                                self.turn_record.append(current_player)
                                sleep(0.5)
                                print(str(self.players[i].name)
                                      + "'s current position is "
                                      + str(self.players[i].position)
                                      + ".")

                    else:
                        if current_player == self.players[0].name:
                            self.players[i].position += roll
                            self.turn_record.append(current_player)
                            sleep(0.5)
                            print(str(self.players[i].name)
                                  + "'s current position is "
                                  + str(self.players[i].position)
                                  + ".")
                        else:
                            print("It is not your turn. It is "
                                  + str(self.players[0].name)
                                  + "'s turn.")
                else:
                    if (self.turn_record[-1] != current_player
                            and self.turn_record[-2] != current_player):
                        self.players[i].position += roll
                        self.turn_record.append(current_player)
                        sleep(0.5)
                        print(str(self.players[i].name)
                              + "'s current position is "
                              + str(self.players[i].position)
                              + ".")
            elif (self.players[i].name == current_player
                  and self.players[i].position + roll > 100):
                self.turn_record.append(current_player)
                print("Your roll is invalid! You need to roll a "
                      + str(100 - self.players[i].position)
                      + " in order to win. You rolled a "
                      + str(roll) + ". Your turn has been skipped.")

    def add_player(self, player1: Player, player2: Player) -> None:
        """Add a player to the board, with 2 players required."""
        if len(self.players) != 2:
            self.players.append(player1)
            self.players.append(player2)
        else:
            print("You cannot have more than 2 players in this game.")

    def game_start(self) -> None:
        """Start the game."""
        if len(self.players) != 2:
            name1 = input("Please input Player 1's name: ")
            name2 = input("Please input Player 2's name: ")
            p1 = Player(name1)
            p2 = Player(name2)
            self.add_player(p1, p2)
        while not self.winner:
            for player in self.players:
                if (((player.position not in self.licorice_spaces)
                     or (player.position in self.licorice_spaces
                         and self.turn_record[-1] != player.name
                         and self.turn_record[-2] != player.name))
                        and self.winner is False):
                    sleep(0.5)
                    print("")
                    print("It's your turn, " + str(player.name) + ".")
                    s = input("Please press enter or return to continue.")
                elif (self.players[0].position == self.players[1].position
                      and self.players[0].skip_turn
                      and self.players[1].skip_turn):
                    sleep(0.5)
                    print("")
                    print("It's your turn, " + str(player.name) + ".")
                    s = input("Please press enter or return to continue.")
                elif player.skip_turn:
                    sleep(0.5)
                    print("")
                    print(
                        "You are on a licorice space, " + str(player.name) +
                        ". Your turn has been skipped.")
                    player.skip_turn = False
                    s = "."
                if s == "":
                    self.move(player.name)
                    if player.position in self.licorice_spaces:
                        player.skip_turn = True
                    if player.position == 100:
                        print("")
                        print(str(player.name)
                              + " has won the game! Congratulations!")
                        self.winner_record.append(player.name)
                        self.games_played += 1
                        self.winner = True
                        break
        self.winner = False
        print('')
        self.restart_prompt()

    def start_game_again(self) -> None:
        """Start the game again, retaining some of the same values."""
        self.turn_record = []
        self.players[0].position = 0
        self.players[1].position = 0
        while not self.winner:
            for player in self.players:
                if (((player.position not in self.licorice_spaces)
                     or (player.position in self.licorice_spaces
                         and self.turn_record[-1] != player.name
                         and self.turn_record[-2] != player.name))
                        and self.winner is False):
                    sleep(0.5)
                    print("")
                    print("It's your turn, " + str(player.name) + ".")
                    s = input("Please press enter or return to continue.")
                elif (self.players[0].position == self.players[1].position
                      and self.players[0].skip_turn
                      and self.players[1].skip_turn):
                    sleep(0.5)
                    print("")
                    print("It's your turn, " + str(player.name) + ".")
                    s = input("Please press enter or return to continue.")
                elif player.skip_turn:
                    sleep(0.5)
                    print("")
                    print(
                        "You are on a licorice space, " + str(player.name) +
                        ". Your turn has been skipped.")
                    player.skip_turn = False
                    s = "."
                if s == "":
                    self.move(player.name)
                    if player.position in self.licorice_spaces:
                        player.skip_turn = True
                    if player.position == 100:
                        print("")
                        print(str(player.name)
                              + " has won the game! Congratulations!")
                        self.winner_record.append(player.name)
                        self.games_played += 1
                        self.winner = True
                        break
        self.winner = False
        print('')
        self.restart_prompt()

    def restart_prompt(self) -> None:
        """Choose to play the game again."""
        restart = input("Would you like to play again? (Y/N): ")
        if restart == "Y":
            self.start_game_again()
        elif restart == 'N':
            print('Bye bye.')
        else:
            print('Your input was invalid. Please try again.')


b = Board()
