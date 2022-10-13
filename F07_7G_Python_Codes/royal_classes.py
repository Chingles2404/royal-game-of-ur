# F07 Team 7G Members: Chew Ching Hian 1006083, Caroline Tiu 1006179, Leow Jing Ting 1006392, Cordelia Tan 1006138, Nicholas Ng Zhi Yong 1006021

import random



# Space represents specific cells on the board
class Space:
    def __init__(self, space_id, rosette):
        # space_id is a list with 4 elements
        # element 1: ID of space with respect to Player 1
        # element 2: number of pieces Player 1 has on that space
        # element 3: ID of space with respect to Player 2
        # element 4: number of pieces Player 2 has on that space
        self._id = space_id
        # rosette holds a boolean to determine whether that space has a rosette
        self._rosette = rosette
    

    # setter functions
    def set_id(self, space_id):
        self._id = space_id
    
    def set_rosette(self, rosette):
        self._rosette = rosette
    

    # getter functions
    def get_id(self):
        return self._id
    
    def get_rosette(self):  
        return self._rosette
    


# Board represents the entire game board
class Board:
    def __init__(self):
        spaces = []
        for i in range(4):
            # this range of spaces is the first safe zone for each player
            # an example of the ID for the space is as follows:
            # Space 1 with respect to Player 1 will have the ID of [0, 0, None, 0]
            # Space 1 with respect to Player 2 will have the ID of [None, 0, 0, 0]
            # None is used to show that the space cannot be accessed by the player that the ID is with respect to
            # the second and fourth items are initialised as 0 as the players start off with no pieces on any spaces
            space_p1 = [i, 0, None, 0]
            space_p2 = [None, 0, i, 0]
            if i == 3: # this space has a rosette
                spaces.append(Space(space_p1, True))
                spaces.append(Space(space_p2, True))
            else:
                spaces.append(Space(space_p1, False))
                spaces.append(Space(space_p2, False))                
        for i in range(8):
            # this is the combat zone, which both players can access
            # an example of the ID for the space is as follows
            # Space 5 with respect to both players will have the ID of [5, 0, 5, 0]
            space = [i + 4, 0, i + 4, 0]
            if i == 3: # this space has a rosette
                spaces.append(Space(space, True))
            else:
                spaces.append(Space(space, False))
        for i in range(2):
            # this range of spaces is the second safe zone for each player
            # the format follows that of the first safe zone
            space_p1 = [i + 12, 0, None, 0]
            space_p2 = [None, 0, i + 12, 0]
            if i == 1: # this space has a rosette
                spaces.append(Space(space_p1, True))
                spaces.append(Space(space_p2, True))
            else:
                spaces.append(Space(space_p1, False))
                spaces.append(Space(space_p2, False)) 
        self._spaces = spaces
    

    # setter functions
    def set_spaces(self, spaces):
        self._spaces = spaces
    

    # getter functions
    def get_spaces(self):
        return self._spaces



# Player represents a player playing the game
class Player:
    def __init__(self, player_id, total):
        # this is an integer that holds a value of 1 or 2
        # it represents the ID of the player since there are only 2 players
        self._id = player_id
        # this is an integer that represents the total number of pieces that the player has
        self._total = total
        # this is an integer that represents the number of playable pieces the player has that are off the board
        # it is initialised to be the same value has self._total
        # this is because the player starts the game with all their pieces off the board
        self._off_board = total
        # this is a list that contains integers that represent the positions of the pieces with respect to the player that the player currently has on the board
        # this is initialised as an empty list since the player starts with no pieces on the board
        self._on_board = []
        # this is an integer that represents the number of pieces that are home and have completed a course on the board
        # these pieces are no longer playable after they are home
        # this is initialised as 0 since the player starts with no pieces that are home
        self._home = 0
    
    
    # setter functions
    def set_id(self, player_id):
        self._id = player_id
    
    def set_total(self, total):
        self._total = total

    def set_off_board(self, off_board):
        self._off_board = off_board

    def set_on_board(self, on_board):
        self._on_board = on_board

    def set_home(self, home):
        self._home = home
    

    # getter functions
    def get_id(self):
        return self._id
    
    def get_total(self):
        return self._total
    
    def get_off_board(self):
        return self._off_board
    
    def get_on_board(self):
        return self._on_board

    def get_home(self):
        return self._home



# Game contains the game logic
class Game:
    def __init__(self, number_of_pieces):
        # this is an integer that represents the total number of pieces that each player has
        self._number_of_pieces = number_of_pieces
        # this is a Player object for the first player
        # thus this is initialised with a player_id of 1 and a total of number_of_pieces
        self._player1 = Player(1, number_of_pieces)
        # this is a Player object for the second player
        # thus this is initialised with a player_id of 2 and a total of number_of_pieces
        self._player2 = Player(2, number_of_pieces)
        # this is a Board object for the game board
        self._board = Board()
    

    # setter functions
    def set_number_of_pieces(self, number_of_pieces):
        self._number_of_pieces = number_of_pieces
    
    def set_player1(self, player1):
        self._player1 = player1
    
    def set_player2(self, player2):
        self._player2 = player2
    
    def set_board(self, board):
        self._board = board
    

    # getter functions
    def get_number_of_pieces(self):
        return self._number_of_pieces
    
    def get_player1(self):
        return self._player1
    
    def get_player2(self):
        return self._player2
    
    def get_board(self):
        return self._board
        

    # this function is used if the player chooses to move a piece that is already on the board
    def move_piece(self, player_id, dice_roll, init_space_id):
        # determine which player object to use based on the player we are currently looking at (from the player_id)
        if player_id == 1:
            # this contains the object of the player we are looking at
            player = self._player1
            # this contains the object of the player's opponent
            opp_player = self._player2
            # this is the index to get the ID of a space with respect to the player we are looking at (1st element)
            space_id = 0
            # this is the index to get the ID of a space with respect to the player's opponent (3rd element)
            space_id_opp = 2
        elif player_id == 2:
            # this contains the object of the player we are looking at
            player = self._player2
            # this contains the object of the player's opponent
            opp_player = self._player1
            # this is the index to get the ID of a space with respect to the player we are looking at (1st element)
            space_id = 2
            # this is the index to get the ID of a space with respect to the player's opponent (3rd element)
            space_id_opp = 0
        else:
            # an error is generated if the player_id is not 1 or 2
            print("Invalid PlayerID. Input only values 1 or 2.")
            return False, None
        
        # this will eventually contain a Space object of the space that the player's piece is currently on
        init_space = None
        # this will eventually contain a Space object of the space that the player's piece is moving to
        final_space = None
        # this is to find the ID of the final space with respect to the player
        final_space_id = init_space_id + dice_roll

        # check whether the move is valid
        # the ID of the spaces go up to 13
        # 14 is included so that the pieces can go home
        # note that the piece can only go home if the dice roll is exactly the number of spaces needed
        # therefore it needs to be less than or equal to 14
        if init_space_id + dice_roll <= 14:
            # this is the counter for the while loop below
            i = 0
            # this while loop is used to find the Space objects for init_space and final_space
            while i < len(self._board.get_spaces()):
                # this contains the list of Space objects that the Board object has
                spaces = self._board.get_spaces()

                # find the space where the player's piece is currently on
                if spaces[i].get_id()[space_id] == init_space_id:
                    # assign the Space object that has the same ID as init_space_id to init_space
                    init_space = spaces[i]

                    # check whether the player has any piece to move from the space
                    if init_space.get_id()[space_id + 1] == 0:
                        # throw an error if there is no piece belonging to the player on that space
                        print("No pieces to move.")
                        return False, None
                    
                # find the space where the player's piece will end on
                elif spaces[i].get_id()[space_id] == final_space_id:
                    # assign the Space object that has the same ID as final_space_id to final_space
                    final_space = spaces[i]

                    # check whether the player already has a piece on this space
                    if final_space.get_id()[space_id + 1] > 0:
                        # throw an error if there is already a piece belonging to the player on that space
                        print("You already have a piece in this space.")
                        return False, None
                    
                    # check whether the player is landing on the rosette in the combat area
                    # and check whether the player's opponent already has a piece on the space with the rosette in the combat area
                    # if the player's opponent has a piece on that space, the player's piece will move to the space in front of it
                    elif final_space.get_id()[space_id] == 7 and final_space.get_id()[space_id_opp + 1] > 0 and final_space.get_rosette():
                        # notify the user of the change in final position
                        print("Your opponent has a piece here, so your piece will be shifted to the next space.")
                        # change the final_space_id to the space in front of the rosette in the combat zone if it is not occupied
                        # no need to place a check to make sure that the next space is within range because the board layout shows it definitely is
                        final_space_id += 1
                        # change the counter to -1 (so that i = 0 on the next iteration) to restart iteration to find the new final space
                        i = -1
                
                # this is the increment for the iteration
                i += 1
            
            # this is a list of the positions of the player's pieces on the board
            pieces = player.get_on_board()
            # remove the element containing the position of the moved piece (since we are moving one piece)
            if init_space.get_id()[space_id] in player.get_on_board():
                pieces.remove(init_space.get_id()[space_id])
            
            # check whether the selected piece will be home
            if init_space_id + dice_roll == 14:
                # create a temporary variable using the ID of the initial space (which is a list)
                temp_id = init_space.get_id()
                # space_id + 1 since the item representing player's pieces is one index after the item containing the ID of the space with respect to the player
                # reduce the number of pieces that the player has in that space by 1
                temp_id[space_id + 1] -= 1
                # update the ID of the initial space
                init_space.set_id(temp_id)
                # increase the number of pieces that the player has that are home by 1
                player.set_home(player.get_home() + 1)
            else:
                # check whether the piece will land on a space within the combat zone
                if final_space.get_id()[space_id_opp + 1] != None:
                    # knocking out opponent's pieces
                    # increase the number of pieces that the opponent has off the board by the number of pieces the opponent had on the space that is now occupied by the player
                    # this should be 1, but leaving it as a variable allows for changes in game rules to be implemented more easily
                    opp_player.set_off_board(opp_player.get_off_board() + final_space.get_id()[space_id_opp + 1])
                    # get the list of positions of pieces that the opponent currently has on the board
                    opp_pieces = opp_player.get_on_board()
                    # remove all occurrences of the opponent's pieces in the space where the player is at now
                    # this is because all of the opponent's pieces will be moved off the board
                    for i in range(opp_player.get_on_board().count(final_space.get_id()[space_id_opp])):
                        opp_pieces.remove(final_space.get_id()[space_id_opp])
                    # update the list of positions of the opponent's pieces
                    opp_player.set_on_board(opp_pieces)
                
                # create a temporary variable using the ID of the initial space (which is a list)
                temp_i_id = init_space.get_id()
                # space_id + 1 since the item representing player's pieces is one index after the item containing the ID of the space with respect to the player
                # reduce the number of pieces that the player has in that space by 1
                temp_i_id[space_id + 1] -= 1
                # create a temporary variable using the ID of the final space (which is a list)
                temp_f_id = final_space.get_id()
                # space_id + 1 since the item representing player's pieces is one index after the item containing the ID of the space with respect to the player
                # increase the number of pieces that the player has in that space by 1
                temp_f_id[space_id + 1] += 1
                # change the number of pieces that the opponent has in that space to 0
                temp_f_id[space_id_opp + 1] = 0
                # update the ID of the initial space
                init_space.set_id(temp_i_id)
                # update the ID of the final space
                final_space.set_id(temp_f_id)
                # add the new position of the piece on the board to the list of positions of player's pieces on the board
                pieces.append(final_space.get_id()[space_id])
                pieces.sort()
                # update the list
                player.set_on_board(pieces)
        else:
            # throw an error if the final space exceeds 14
            print("Cannot move to this space.")
            return False, None
        
        # this will only run if none of the errors were raised
        print("Piece has been moved.")
        return True, final_space
    
    # this function is used if the player chooses to add a piece to the board
    def add_piece(self, player_id, dice_roll):
        if dice_roll - 1 > 14:
            # throw an error if the final space exceeds 14
            print("Cannot move to this space, dice roll is too large.")
            return False, None
        else:
            # determine which player object to use based on the player we are currently looking at (from the player_id)
            if player_id == 1:
                # this contains the object of the player we are looking at
                player = self._player1
                # this contains the object of the player's opponent
                opp_player = self._player2
                # this is the index to get the ID of a space with respect to the player we are looking at (1st element)
                space_id = 0
                # this is the index to get the ID of a space with respect to the player's opponent (3rd element)
                space_id_opp = 2
            elif player_id == 2:
                # this contains the object of the player we are looking at
                player = self._player2
                # this contains the object of the player's opponent
                opp_player = self._player1
                # this is the index to get the ID of a space with respect to the player we are looking at (1st element)
                space_id = 2
                # this is the index to get the ID of a space with respect to the player's opponent (3rd element)
                space_id_opp = 0
            else:
                # an error is generated if the player_id is not 1 or 2
                print("Invalid PlayerID. Input only values 1 or 2.")
                return False, None
            
            # this is to find the ID of the final space with respect to the player
            # subtracting 1 is necessary since we are starting from off the board which can be thought of as the -1th position
            # as such, the final_space_id is essentially (-1) + dice_roll which is the dice roll added to the initial ID
            final_space_id = dice_roll - 1

            # this checks if the player has any pieces to add to the board
            if player.get_off_board() > 0:
                # this is the counter for the while loop below
                i = 0
                # this while loop is to find the Space object for the space the piece ends on
                while i < len(self._board.get_spaces()):
                    # this contains the list of Space objects that the Board object has
                    spaces = self._board.get_spaces()
                    # find the space where the piece will end on
                    if spaces[i].get_id()[space_id] == final_space_id:
                        # assign the Space object that has the same ID as final_space_id to space
                        space = spaces[i]
                        # check whether the player already has pieces on this space
                        if space.get_id()[space_id + 1] > 0:
                            # throw an error if there are already pieces belonging to the player on that space
                            print("You already have a piece in this space.")
                            return False, None
                        
                        # check whether the player is landing on the rosette in the combat area
                        # and check whether the player's opponent already has a piece on the space with the rosette in the combat area
                        # if the player's opponent has a piece on that space, the player's piece will move to the space in front of it
                        elif space.get_id()[space_id] == 7 and space.get_id()[space_id_opp + 1] > 0 and space.get_rosette():
                            # notify the user of the change in final position
                            print("Your opponent has a piece here, so your piece will be shifted to the next space.")
                            # change the final_space_id to the space in front of the rosette in the combat zone if it is not occupied
                            # no need to place a check to make sure that the next space is within range because the board layout shows it definitely is
                            final_space_id += 1
                            # change the counter to -1 (so that i = 0 on the next iteration) to restart iteration to find the new final space
                            i = -1

                        else: 
                            # check whether the piece will land on a space within the combat zone
                            if space.get_id()[space_id_opp + 1] != None:
                                # increase the number of pieces that the opponent has off the board by the number of pieces the opponent had on the space that is now occupied by the player
                                # this should be 1, but leaving it as a variable allows for changes in game rules to be implemented more easily
                                opp_player.set_off_board(opp_player.get_off_board() + space.get_id()[space_id_opp + 1])
                                # get the list of positions of pieces that the opponent currently has on the board
                                opp_pieces = opp_player.get_on_board()
                                # remove all occurrences of the pieces in the space where the player is at now
                                # this is because all of the opponent's pieces will be moved off the board
                                for i in range(opp_player.get_on_board().count(space.get_id()[space_id_opp])):
                                    opp_pieces.remove(space.get_id()[space_id_opp])
                                # update the list of positions of the opponent's pieces
                                opp_player.set_on_board(opp_pieces)
                            
                            # create a temporary variable using the ID of the final space (which is a list)
                            temp_id = space.get_id()
                            # space_id + 1 since the item representing player's pieces is one index after the item containing the ID of the space with respect to the player
                            # increase the number of pieces that the player has in that space by 1
                            temp_id[space_id + 1] += 1
                            # update the ID of the final space
                            space.set_id(temp_id)
                            # this is a list of the positions of the player's pieces on the board
                            pieces = player.get_on_board()
                            # add the new position of the piece on the board to the list of positions of pieces on the board
                            pieces.append(space.get_id()[space_id])
                            pieces.sort()
                            # update the list
                            player.set_on_board(pieces)
                            # update the number of pieces that the player has off the board
                            player.set_off_board(player.get_off_board() - 1)
                            return True, space
                    # this is the increment for the iteration
                    i += 1
            else:
                # an error is thrown if there are no pieces off the board
                print("No pieces to add to the board.")
                return False, None
    
    # checking if the space the player has landed on has a rosette
    def check_rosette(self, space):
        # check if space is not a None value
        if space != None:
            # return the rosette attribute of the space
            return space.get_rosette()
        else:
            # return False since it means that the space definitely does not have a rosette since it is not even a space
            return False

    # this rolls the dice and returns an integer
    def roll_dice(self):
        # this is the total dice value
        total = 0
        for i in range(4):
            # since each die in the original game has a 50-50 chance of rolling the value 1 or 0, randint should be used
            total += random.randint(0, 1)
        return total
    
    # this checks whether either of the players have won and returns a boolean
    def check_wincon(self):
        # check whether either of the players have gotten all their pieces home
        # if True, display a congratulatory message for the winning player
        if self._player1.get_home() == self._player1.get_total():
            print("Congratulations, Player 1, you won the game! Bask in the gloryyy!")
            return True
        elif self._player2.get_home() == self._player2.get_total():
            print("Congratulations, Player 2, you won the game! Bask in the gloryyy!")
            return True
        else:
            return False