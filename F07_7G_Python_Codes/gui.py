# F07 Team 7G Members: Chew Ching Hian 1006083, Caroline Tiu 1006179, Leow Jing Ting 1006392, Cordelia Tan 1006138, Nicholas Ng Zhi Yong 1006021

from tkinter import *

# constants for GUI
height = 300
width = 800
rows = 3
columns = 8
cell_width = width / columns
cell_height = height / rows

class royal_classes_GUI:
    def __init__(self):
        self.root = Tk()
        self.background = Canvas(self.root, bg = "Black", width = 800, height = 300)
        self.background.grid()


    def grid(self):
        # creating the board by looping columns and rows 
        # removes 4th and 5th square in the first and third row accoring to the layout of the board
        for i in range(columns):
            for j in range(rows):
                if (i == 4 or i == 5) and (j == 0 or j == 2):
                    self.background.create_rectangle(i * cell_width, j * cell_height, (i + 1) * cell_width, (j + 1) * cell_height, fill="Black")
                else:
                    self.background.create_rectangle(i * cell_width, j * cell_height, (i + 1) * cell_width, (j + 1) * cell_height, fill="White")
                    self.background.pack()
                    
        # creating rosettes
        self.background.create_text(15, 15, text='*', font = "Arial 25") # top left
        self.background.create_text(15, 15 + 2 * cell_height, text='*', font = "Arial 25") # bottom left
        self.background.create_text(15 + 3 * cell_width, 15 + cell_height, text='*', font = "Arial 25") # center
        self.background.create_text(15 + 6 * cell_width, 15, text='*', font = "Arial 25") # top right
        self.background.create_text(15 + 6 * cell_width, 15 + 2 * cell_height, text='*', font = "Arial 25") # bottom right
        self.background.pack()
    
    def number_player1(self):
        # this creates the numbering for player 1 from 0 to 13

        # (player 1) numbering 0-3
        count1 = 0
        for i in range(3,-1,-1):
            self.background.create_text(
                (i*cell_width) + cell_width/2, 10,
                font= "Impactlight 10",
                text= count1,
                tag='txt',
                fill = "Blue"
            )
            count1 += 1
        
        # (player 1) numbering combat zone
        count2 = 4
        for i in range(columns):
            self.background.create_text(
                cell_width/2 + (i*cell_width), cell_height + 10,
                font= "Impactlight 10",
                text= count2,
                tag='txt',
                fill = "Blue"
            )
            count2 += 1
            
        # (player 1) numbering 12 and 13
        count3 = 12
        for i in range(13,11,-1):
            self.background.create_text(
                ((i-5)*cell_width)- cell_width/2, 10,
                font= "Impactlight 10",
                text= count3,
                tag='txt',
                fill = "Blue"
            )
            count3 += 1           

       
    def number_player2(self):
    # this creates the numbering for player 2 from 0 to 13
        # (player 2) numbering 0-3
        count1 = 0
        for i in range(3,-1,-1):
            self.background.create_text(
                (i*cell_width) + cell_width/2, 3*cell_height - 10,
                font= "Impactlight 10",
                text= count1,
                tag='txt',
                fill = "Red"
            )
            count1 += 1       
        
        # (player 2) numbering combat zone
        count2 = 4
        for i in range(columns):
            self.background.create_text(
                cell_width/2 + (i*cell_width), 2*cell_height - 10,
                font= "Impactlight 10",
                text= count2,
                tag='txt',
                fill = "Red"
            )
            count2 += 1
            
        # (player 2) numbering 12 and 13   
        count3 = 12
        for i in range(13,11,-1):
            self.background.create_text(
                ((i-5)*cell_width)- cell_width/2, 3*cell_height - 10,
                font= "Impactlight 10",
                text= count3,
                tag='txt',
                fill = "Red"
            )
            count3 += 1
    

    def menu_button(self):
        # this create a button at the bottom right of the screen for the user to close the window 
        quit_game = Button(self.root, text = "Close Window", fg ='red', command = self.root.destroy) 
        quit_game.pack(side = RIGHT) 
    
board_display = royal_classes_GUI()
board_display.grid()
board_display.number_player1()
board_display.number_player2()
board_display.menu_button()
board_display.root.mainloop()