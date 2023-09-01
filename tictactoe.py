import tkinter as tk
import random

buttons = None
human = 'X'
computer = 'O'
label = None


def create_tic_tac_toe_ui():
    window = tk.Tk()
    window.title("Tic-Tac-Toe")
    global buttons
    buttons = []
    for i in range(3):
        row = []
        for j in range(3):
            button = tk.Button(window, text=" ", font=("normal", 20), width=5, height=2,
                               command=lambda i=i, j=j: human_move(i, j))
            button.grid(row=i, column=j)
            row.append(button)
        buttons.append(row)
    global label
    label = tk.Label(text="Let the Game Begin!!")
    label.grid(row=5, column=0, columnspan=3)

    window.mainloop()


def is_available(i, j):
    return buttons[i][j]['text'] == ' '


def check_win():
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != ' ':
            return True
    for j in range(3):
        if buttons[0][j]['text'] == buttons[1][j]['text'] == buttons[2][j]['text'] != ' ':
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != ' ':
        return True
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != ' ':
        return True
    return False


def check_draw():
    for i in range(3):
        for j in range(3):
            if buttons[i][j]['text'] == ' ':
                return False
    return True


def insert(letter, i, j):
    if is_available(i, j):
        buttons[i][j]['text'] = letter
        if check_win():
            if letter == 'X':
                label.config(text="Human Wins!!")
            else:
                label.config(text="Computer Wins!!")
            # Disable buttons when the game is over
            for row in buttons:
                for button in row:
                    button.config(state=tk.DISABLED)
        elif check_draw():
            label.config(text="Draw")


def human_move(i, j):
    insert(human, i, j)
    if not check_win() and not check_draw():
        computer_move(computer)


def computer_move(letter):
    while True:
        i = random.randint(0, 2)
        j = random.randint(0, 2)
        if is_available(i, j):
            insert(letter, i, j)
            break


create_tic_tac_toe_ui()