import tkinter as tk
import tkinter.messagebox
from tkinter import *

special = False
root = tk.Tk()
root.geometry('300x300')
player_turn = True
counter = 0
nameOne = StringVar()
nameTwo = StringVar()
winner = nameOne

def button_click(but):
    but.configure(state=DISABLED)

def game_end():
    global winner
    if special == True:
        special_result = messagebox.askquestion("Oh no!", "Do You want to play again?")
        if special_result == 'yes':
            reset()
        else:
            exit()
    else:
        result = messagebox.askquestion("Congratulation's!  " + winner.get(), "Do You want to play again?")
        if result == 'yes':
            reset()
        else:
            exit()

def reset():
    global counter, player_turn
    counter = 0
    player_turn = True
    button1.configure(state=NORMAL, text=" ")
    button2.configure(state=NORMAL, text=" ")
    button3.configure(state=NORMAL, text=" ")
    button4.configure(state=NORMAL, text=" ")
    button5.configure(state=NORMAL, text=" ")
    button6.configure(state=NORMAL, text=" ")
    button7.configure(state=NORMAL, text=" ")
    button8.configure(state=NORMAL, text=" ")
    button9.configure(state=NORMAL, text=" ")



def main_game(which_button):
    global player_turn, counter, winner, nameOne, nameTwo
    if player_turn == True:
        which_button["text"] = "X"
        player_turn = False
        button_click(which_button)
        counter += 1
        winner = nameOne
        check()
    else:
        which_button["text"] = "O"
        player_turn = True
        button_click(which_button)
        counter +=1
        winner = nameTwo
        check()

def check():
    global special
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
        button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
        button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
        button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
        button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
        button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
        button7['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        game_end()


    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
          button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
          button7['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
        game_end()

    elif(counter == 9):
        special = True
        game_end()

label1 = Label(root, text="Player 1:")
label1.grid(row=1,column=3)
label2 = Label(root, text="Player 2:")
label2.grid(row=2,column=3)
playerOne = Entry(root, textvariable=nameOne, bd=5)
playerOne.grid(row=1, column=4)
playerTwo = Entry(root, textvariable=nameTwo, bd=5)
playerTwo.grid(row=2, column=4)

button1 = tk.Button(root, text=" ", font="Times 10 bold", bg="white", fg="white", height=2, width=4, command=lambda: main_game(button1))
button1.grid(row=1, column=0)
button2 = tk.Button(root, text=" ", font="Times 10 bold", bg="white", fg="white", height=2, width=4, command=lambda: main_game(button2))
button2.grid(row=1, column=1)
button3 = tk.Button(root, text=" ", font="Times 10 bold", bg="white", fg="white", height=2, width=4, command=lambda: main_game(button3))
button3.grid(row=1, column=2)
button4 = tk.Button(root, text=" ", font="Times 10 bold", bg="white", fg="white", height=2, width=4, command=lambda: main_game(button4))
button4.grid(row=2, column=0)
button5 = tk.Button(root, text=" ", font="Times 10 bold", bg="white", fg="white", height=2, width=4, command=lambda: main_game(button5))
button5.grid(row=2, column=1)
button6 = tk.Button(root, text=" ", font="Times 10 bold", bg="white", fg="white", height=2, width=4, command=lambda: main_game(button6))
button6.grid(row=2, column=2)
button7 = tk.Button(root, text=" ", font="Times 10 bold", bg="white", fg="white", height=2, width=4, command=lambda: main_game(button7))
button7.grid(row=3, column=0)
button8 = tk.Button(root, text=" ", font="Times 10 bold", bg="white", fg="white", height=2, width=4, command=lambda: main_game(button8))
button8.grid(row=3, column=1)
button9 = tk.Button(root, text=" ", font="Times 10 bold", bg="white", fg="white", height=2, width=4, command=lambda: main_game(button9))
button9.grid(row=3, column=2)


root.mainloop()
