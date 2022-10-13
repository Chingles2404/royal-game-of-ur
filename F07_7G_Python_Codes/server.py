# F07 Team 7G Members: Chew Ching Hian 1006083, Caroline Tiu 1006179, Leow Jing Ting 1006392, Cordelia Tan 1006138, Nicholas Ng Zhi Yong 1006021

import socket, royal_classes, socket_func

ssock = socket.socket()
ssock.bind(('', 12345)) # replace IP address before gameplay
ssock.listen()

csock, address = ssock.accept()

game = royal_classes.Game(7)

# variable to break the while loop later on
running = True



# first die roll to determine which player goes first
dice_roll = game.roll_dice()
print(dice_roll)
# listening to client socket to get client's first die roll
client = b''
while b'\n' not in client:
    client += csock.recv(1024)
if b'ROLL' in client:
    client = int(client.decode()[5:-1])
    print(client)

# reroll until one player gets a higher dice value than the other
while dice_roll == client:
    csock.sendall(b'REROLL\n')
    dice_roll = game.roll_dice()
    print(dice_roll)
    # listening to client socket to get client's die roll
    client = b''
    while b'\n' not in client:
        client += csock.recv(1024)
    client = client.decode()
    if 'ROLL' in client:
        client = int(client[5:-1])
        print(client)

# logic to determine which player goes first
if client > dice_roll:
    # setting player IDs
    player_id = 2
    opp_player_id = 1

    # telling the client that they start first
    csock.sendall(b'START\n')
    
    # listening to client socket to get client's move
    client = b''
    while b'\n' not in client and running:
        client += csock.recv(1024)
    # check whether the game is still running
    if running:
        # decode the message since it is encoded in bytes
        client = client.decode()
        running = socket_func.read_message(running, game, client, opp_player_id)
else:
    # setting player IDs
    player_id = 1
    opp_player_id = 2




# loop that runs while the socket is open
while running:
    # check whether client has won
    if game.check_wincon() and running:
        print("GAME OVER.")
        running = False
    
    running = socket_func.send_message(running, game, csock, player_id)

    # check whether server has won
    if game.check_wincon() and running:
        print("GAME OVER.")
        running = False

    if running:
        # listening to the socket to get client's move
        client = b''
        while b'\n' not in client:
            client += csock.recv(1024)
        # decode the message since it is encoded in bytes
        client = client.decode()
        running = socket_func.read_message(running, game, client, opp_player_id)

csock.close()
ssock.close()
