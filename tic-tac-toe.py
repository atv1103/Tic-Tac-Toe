from tkinter import *
import random

#main window settings
root = Tk()
root.title("Tic-Tac-Toe")
root.resizable(False, False)  # prohibition of resizing window
game_running = True
field = []
cross_count = 0 #for draw

def new_game():
    global game_running
    global cross_count
    game_running = True
    cross_count = 0
    for row in range(3):
        for col in range(3):
            field[row][col]["text"] = " "
            field[row][col]["background"] = "lavender"

#main design
for row in range(3):
    line = []
    for col in range(3):
        button = Button(root, text=" ", width=4, height=2, font=("Verdana", 20, "bold"),bg="lavender", command=lambda row=row, col=col: click(row,col))
        button.grid(row=row, column=col, sticky="nsew")
        line.append(button)
    field.append(line)
new_button = Button(root, text="new game", command=new_game)
new_button.grid(row=3, column=0, columnspan=3, sticky="nsew")

#buttons click function
def click(row, col):
    global cross_count
    if game_running and field[row][col]["text"] == " ":
        field[row][col]["text"] = "X"
        cross_count += 1
        check_win("X")
        if game_running and cross_count < 5:
            computer_move()
            check_win("O")

#check victory
def check_win(smb):
    for n in range(3):
        check_line(field[n][0], field[n][1], field[n][2], smb) #check row
        check_line(field[0][n], field[1][n], field[2][n], smb) #check column
    check_line(field[0][0], field[1][1], field[2][2], smb) #check diagonal from upper left to right down
    check_line(field[2][0], field[1][1], field[0][2], smb) #check diagonal from left down to upper right

def check_line(a1,a2,a3,smb):
    global game_running
    if a1["text"] == smb and a2["text"] == smb and a3["text"] == smb:
        a1["background"] = a2["background"] = a3["background"] = "pink"
        game_running = False

#II action
def can_win(a1,a2,a3,smb):
    result = False
    if a1["text"] == smb and a2["text"] == smb and a3["text"] == " ":
        a3["text"] = "O"
        result = True
    if a1["text"] == smb and a2["text"] == " " and a3["text"] == smb:
        a2["text"] = "O"
        result = True
    if a1["text"] == " " and a2["text"] == smb and a3["text"] == smb:
        a1["text"] = "O"
        result = True
    return result

def computer_move():
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], "O"):
            return
        if can_win(field[0][n], field[1][n], field[2][n], "O"):
            return
    if can_win(field[0][0], field[1][1], field[2][2], "O"):
        return
    if can_win(field[2][0], field[1][1], field[0][2], "O"):
        return
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], "X"):
            return
        if can_win(field[0][n], field[1][n], field[2][n], "X"):
            return
    if can_win(field[0][0], field[1][1], field[2][2], "X"):
        return
    if can_win(field[2][0], field[1][1], field[0][2], "X"):
        return
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if field[row][col]["text"] == " ":
            field[row][col]["text"] = "O"
            break


root.mainloop()
