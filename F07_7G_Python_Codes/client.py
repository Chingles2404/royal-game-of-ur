# F07 Team 7G Members: Chew Ching Hian 1006083, Caroline Tiu 1006179, Leow Jing Ting 1006392, Cordelia Tan 1006138, Nicholas Ng Zhi Yong 1006021

import socket, royal_classes, socket_func
csock = socket.socket()
csock.connect(('127.0.0.1', 12345)) # replace IP address before gameplay

game = royal_classes.Game(7)

running = True

# first die roll to determine which player goes first
dice_roll = game.roll_dice()
print(dice_roll)
client = dice_roll
if running:
    csock.sendall('ROLL,{}\n'.format(dice_roll).encode())

player_id = 2
opp_player_id = 1

# loop that runs while the socket is open
while running:
    # listening to the socket to get server's move
    server = b''
    while b'\n' not in server and running:
        server += csock.recv(1024)
    if running:
        # decode the message since it is encoded in bytes
        server = server.decode()
        if "START" in server:
            player_id = 1
            opp_player_id = 2
        elif "REROLL" in server:
            dice_roll = game.roll_dice()
            print(dice_roll)
            client = dice_roll
            if running:
                csock.sendall('ROLL,{}\n'.format(dice_roll).encode())
        else:
            running = socket_func.read_message(running, game, server, opp_player_id)

    # check whether server has won
    if game.check_wincon() is True and running:
        print("GAME OVER.")
        running = False

    running = socket_func.send_message(running, game, csock, player_id)

    # check whether client has won
    if game.check_wincon() is True and running:
        print("GAME OVER.")
        running = False

csock.close()
    
