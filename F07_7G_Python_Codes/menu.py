# F07 Team 7G Members: Chew Ching Hian 1006083, Caroline Tiu 1006179, Leow Jing Ting 1006392, Cordelia Tan 1006138, Nicholas Ng Zhi Yong 1006021

# validate the input that was entered in response to the main menu
def validate_main_opt(opt, moves):
    # presence check
    # this is to check whether an input has been entered
    if len(opt) == 0:
        print("No input received.")
        return False
    # type check
    # this is to check that the player only entered a numerical input
    elif not opt.isdigit():
        print("Please type a numeric option.")
        return False
    # range check
    # this is to check that the player selected a valid option
    elif int(opt) < 1 or int(opt) > moves:
        print("No such option exists.")
        return False
    # the else statement only runs if all of the above conditions were not satisfied
    # this means that the input is valid
    else:
        print("Option received.")
        return True



# prompt the player to choose which piece they wish to move
# and validate the input that was entered in response to the prompt
# pieces takes in a list of the positions of the pieces the player has on the board
def move_input(pieces):
    print("Which piece do you want to move?")
    # show the list of positions that indicates where the player's pieces are on the board
    print(pieces)
    # players choose which piece to move from options which reference their piece's position on the board
    for i in range(len(pieces)):
        print(str(i + 1) + ") Position " + str(pieces[i]))
    
    valid_input = False
    # validate the input that was entered in response to the prompt
    # this loop runs until the player enters a valid input
    while not valid_input:
        # prompt the player for their input
        opt = input()
        # presence check
        # this is to check whether an input has been entered
        if len(opt) == 0:
            print("No input received.")
        # type check
        # this is to check that the player only entered a numerical input
        elif not opt.isdigit():
            print("Please type a numeric option.")
        # range check
        # this is to check that the player selected a valid option
        elif int(opt) < 1 or int(opt) > len(pieces):
            print("No such option exists.")
        # the else statement only runs if all of the above conditions were not satisfied
        # this means that the input is valid
        else:
            print("Option received.")
            valid_input = True
    # this returns the ID of the space where the piece the player has chosen to move is on
    # note that the ID is with respect to the player only (and not the opponent)
    return pieces[int(opt) - 1]



# displays the menu
# off is an integer representing the number of pieces that are off the board
# num is an integer representing the number of pieces that are on the board
def print_menu(off, num):
    print("Choose from the following options for your next move: ")
    # this will contain a list of possible options
    lst_moves = []
    
    # only display the option to move a piece if there are pieces on the board
    if num > 0:
        lst_moves.append("Move a piece on the board.")
    # only display the option to add a piece if there are pieces that are off the board
    if off > 0:
        lst_moves.append("Add a piece on the board.")
    # the following two options will always be displayed
    lst_moves.append("Pass the turn (if other game options are not applicable).")
    lst_moves.append("Quit the game.")

    # this displays the options
    for i in range(len(lst_moves)):
        print("{}) ".format(i + 1) + lst_moves[i])
    return lst_moves



# main menu function
# off is an integer representing the number of pieces that are off the board
# pieces takes in a list of the positions of the pieces the player has on the board
# dice_roll is an integer representing the value of the dice roll
def menu(off, pieces, dice_roll):
    # get the list of possible options the player has
    lst_moves = print_menu(off, len(pieces))
    # variable that will be used to check whether the player's input is valid
    valid_input = False
    # this loop runs until the player gives a valid input
    while not valid_input:
        # prompt the player for input
        opt = input()
        # get the result of the check for whether the input is valid
        valid_input = validate_main_opt(opt, len(lst_moves))
    # get the option that the player has chosen
    move = lst_moves[int(opt) - 1]
    
    # check which option the player has chosen to decide which protocol to use
    # note that the semicolon (;) denotes the end of a protocol
    if "Move" in move:
        # prompt the user for which piece they wish to move
        piece = move_input(pieces)
        # return the MOVE protocol with the space ID where the selected piece is at and the value of the dice roll
        return "MOVE,{},{};".format(piece, dice_roll)
    elif "Add" in move:
        # return the ADD protocol with the value of the dice roll
        return "ADD,{};".format(dice_roll)
    elif "Pass" in move:
        # return the PASS protocol
        return "PASS;"
    else:
        # return the QUIT protocol
        return "QUIT;"