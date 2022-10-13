# F07 Team 7G Members: Chew Ching Hian 1006083, Caroline Tiu 1006179, Leow Jing Ting 1006392, Cordelia Tan 1006138, Nicholas Ng Zhi Yong 1006021

import menu

# this function creates the message that will be sent to the server/client from the client/server
# running is a boolean that determines whether the game is still running
# passed is a boolean that determines whether the player has passed their turn
# game is a Game object from royal_classes.py
# player_id is an integer of value 1 or 2
def create_message(running, passed, game, message, player_id):
    dice_roll = game.roll_dice()
    print("Dice value: " + str(dice_roll))
    if dice_roll == 0:
        print("Automatically passing turn due to dice value being 0.")
        success = True
        passed = True
        # a semicolon (;) denotes the end of a protocol
        message += "PASS;"
    else:
        success = False
    space = None
    # run this portion of code until the player successfully carries out an action
    while not success and running:
        if player_id == 1:
            off_board = game.get_player1().get_off_board()
            pieces = game.get_player1().get_on_board()
        elif player_id == 2:
            off_board = game.get_player2().get_off_board()
            pieces = game.get_player2().get_on_board()
        
        # this displays the menu to the player and prompts them for an input
        option = menu.menu(off_board, pieces, dice_roll)

        # this carries out the game logic and creates the message using the protocol message
        if "MOVE" in option:
            temp = option[:-1].split(",")
            success, space = game.move_piece(player_id, dice_roll, int(temp[1]))
            if success:
                message += option
        elif "ADD" in option:
            success, space = game.add_piece(player_id, dice_roll)
            if success:
                message += option
        elif "PASS" in option:
            message += option
            print("PASSING TURN...")
            passed = True
            success = True
        else:
            message += option
            print("THE GAME HAS BEEN STOPPED.")
            success = True
            running = False
        # display the positions of the pieces that the player currently has on the board
        print(pieces)
    return running, passed, message, space



# this sends the message that was created in the create_message function above
def send_message(running, game, sock, player_id):
    if running:
        print("----------")
        print("YOUR TURN:")
        message = ""
        passed = False
        running, passed, message, space = create_message(running, passed, game, message, player_id)
        # check whether the player has another turn
        while not passed and running and game.check_rosette(space):
            running, passed, message, space = create_message(running, passed, game, message, player_id)
        # end the entire message
        message += "\n"
        sock.sendall(message.encode())
    return running



# this reads what the server/client sent to the client/server
def read_message(running, game, message, opp_player_id):
    if running:
        message = message.split(";")[:-1]
        print("----------")
        print("OPPONENT...")
        # check what action the client has taken
        for i in message:
            if "MOVE" in i:
                temp = i.split(",")
                game.move_piece(opp_player_id, int(temp[2]), int(temp[1]))
                print("Moved piece at Position {} by {} space(s).".format(temp[1], temp[2]))
            elif "ADD" in i:
                temp = i.split(",")
                game.add_piece(opp_player_id, int(temp[1]))
                print("Added a piece to the board, {} space(s) from their start.".format(temp[1]))
            elif "PASS" in i:
                print("Passed their turn.")
            elif "QUIT":
                print("Has quit the game.")
                running = False
        
        if opp_player_id == 1:
            player_id = 2
        elif opp_player_id == 2:
            player_id = 1
        
        # display information for the player on each turn
        print("----------")
        print("Your ID: " + str(player_id))
        print("Opponent's ID: " + str(opp_player_id))
        print("----------")
        print("Total pieces that you have: " + str(game.get_number_of_pieces()))
        print("----------")
        print("Current board:")
        print("Player 1 pieces: " + str(game.get_player1().get_on_board()))
        print("Player 2 pieces: " + str(game.get_player2().get_on_board()))
        print("----------")
        print("Player 1 pieces home: " + str(game.get_player1().get_home()))
        print("Player 2 pieces home: " + str(game.get_player2().get_home()))
        print("----------")
    return running