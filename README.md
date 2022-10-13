# Royal Game of Ur
## Introduction
This was my group's project for our Term 1 module Computational Thinking for Design in the Singapore University of Technology and Design. The task was to create a game with Python using only built-in modules and Tkinter. Our group decided to compromise on the graphics aspect to focus on socket programming to allow the game to be played across two devices. 

The uploaded files are what was submitted, and no edits were made. As such, there are some breaches in coding conventions, particularly in terms of comments.

## Running the Game
The F07_7G_Python_Codes directory should contain the following files:
client.py
gui.py
menu.py
royal_classes.py
socket_func.py
server.py

One player should play through the server, while the other should play through the client.

To start the client, run 
python F07_7G_Python_Codes/client.py

To start the server, run
python F07_7G_Python_Codes/server.py

The server should be started first. To change the server address, modify client.py.
The interface is text-based on the terminal.

To run the sub-interface, run
python F07_7G_Python_Codes/gui.py
(Running this is optional. The sub-interface is a static image that runs independently.)

For more information on how to play this game, refer to F07_7G_Description.pdf and F07_7G_Documentation.pdf.
