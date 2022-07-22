from graphics import *
import random
win = GraphWin('20290122', 300, 350)

#   Drawing TicTacToe Table
for a in range(0, 301, 100):
    b = a
    c = b + 100
    for d in range(0, 301, 100):
        e = d
        f = e + 100
        Rect = Rectangle(Point(b, e), Point(c, f))
        Rect.setOutline("black")
        Rect.setFill("lightgray")
        Rect.draw(win)

Rectan = Rectangle(Point(0, 300), Point(300, 350))
Rectan.setFill("lightgray")
Rectan.draw(win)

sequence = []


#   Board
text1 = Text(Point(50, 50), "O")
text1.setSize(20)
text2 = Text(Point(50, 150), "O")
text2.setSize(20)
text3 = Text(Point(50, 250), "O")
text3.setSize(20)
text4 = Text(Point(150, 50), "O")
text4.setSize(20)
text5 = Text(Point(150, 150), "O")
text5.setSize(20)
text6 = Text(Point(150, 250), "O")
text6.setSize(20)
text7 = Text(Point(250, 50), "O")
text7.setSize(20)
text8 = Text(Point(250, 150), "O")
text8.setSize(20)
text9 = Text(Point(250, 250), "O")
text9.setSize(20)

general_list = []
screen_text = Text(Point(150, 325), "")
screen_text.draw(win)

end_of_game = False


def win_lose_draw():
    global end_of_game
    end_of_game = False
    if text9 in general_list and text5 in general_list and text1 in general_list and sequence[general_list.index(text1)] == sequence[general_list.index(text5)] == sequence[general_list.index(text9)]:
        if sequence[general_list.index(text1)] == "O":
            screen_text.setText("O Wins")
            end_of_game = True
        elif sequence[general_list.index(text1)] == "X":
            screen_text.setText("X Wins")
            end_of_game = True
    if text1 in general_list and text4 in general_list and text7 in general_list and sequence[general_list.index(text1)] == sequence[general_list.index(text4)] == sequence[general_list.index(text7)]:
        if sequence[general_list.index(text1)] == "O":
            screen_text.setText("O Wins")
            end_of_game = True
        elif sequence[general_list.index(text1)] == "X":
            screen_text.setText("X Wins")
            end_of_game = True
    if text3 in general_list and text2 in general_list and text1 in general_list and sequence[general_list.index(text1)] == sequence[general_list.index(text2)] == sequence[general_list.index(text3)]:
        if sequence[general_list.index(text1)] == "O":
            screen_text.setText("O Wins")
            end_of_game = True
        elif sequence[general_list.index(text1)] == "X":
            screen_text.setText("X Wins")
            end_of_game = True
    if text8 in general_list and text5 in general_list and text2 in general_list and sequence[general_list.index(text2)] == sequence[general_list.index(text5)] == sequence[general_list.index(text8)]:
        if sequence[general_list.index(text2)] == "O":
            screen_text.setText("O Wins")
            end_of_game = True
        elif sequence[general_list.index(text2)] == "X":
            screen_text.setText("X Wins")
            end_of_game = True
    if text9 in general_list and text6 in general_list and text3 in general_list and sequence[general_list.index(text3)] == sequence[general_list.index(text6)] == sequence[general_list.index(text9)]:
        if sequence[general_list.index(text3)] == "O":
            screen_text.setText("O Wins")
            end_of_game = True
        elif sequence[general_list.index(text3)] == "X":
            screen_text.setText("X Wins")
            end_of_game = True
    if text7 in general_list and text5 in general_list and text3 in general_list and sequence[general_list.index(text3)] == sequence[general_list.index(text5)] == sequence[general_list.index(text7)]:
        if sequence[general_list.index(text3)] == "O":
            screen_text.setText("O Wins")
            end_of_game = True
        elif sequence[general_list.index(text3)] == "X":
            screen_text.setText("X Wins")
            end_of_game = True
    if text7 in general_list and text8 in general_list and text9 in general_list and sequence[general_list.index(text7)] == sequence[general_list.index(text8)] == sequence[general_list.index(text9)]:
        if sequence[general_list.index(text7)] == "O":
            screen_text.setText("O Wins")
            end_of_game = True
        elif sequence[general_list.index(text7)] == "X":
            screen_text.setText("X Wins")
            end_of_game = True
    if text4 in general_list and text5 in general_list and text6 in general_list and sequence[general_list.index(text4)] == sequence[general_list.index(text5)] == sequence[general_list.index(text6)]:
        if sequence[general_list.index(text4)] == "O":
            screen_text.setText("O Wins")
            end_of_game = True
        elif sequence[general_list.index(text4)] == "X":
            screen_text.setText("X Wins")
            end_of_game = True
    elif len(general_list) == 9:
        screen_text.setText("Draw!")
        end_of_game = True





def random_choice():
    list_of_buttons = [text1, text2, text3, text4, text5, text6, text7, text8, text9]
    choose = random.choice(list_of_buttons)
    if choose in general_list:
        while choose in general_list:
            choose = random.choice(list_of_buttons)
            if len(general_list) == 9:
                break
            elif choose not in general_list:
                choose.draw(win)
                general_list.append(choose)
                sequence.append("O")
                break
    else:
        choose.draw(win)
        general_list.append(choose)
        sequence.append("O")


def quit():
    try:
        q = win.getKey()
        if q == "q" or "Q":
            win.close()
    except:
        win.close()


#   Getting Inputs
while True:
    try:
        z = win.getMouse()
        x = z.getX()
        y = z.getY()
    except:
        break

    #   1
    if 0 < x < 100 and 0 < y < 100:
        screen_text.setText("")
        if text1 not in general_list:
            text1.setText("X")
            text1.draw(win)
            general_list.append(text1)
            sequence.append("X")
            win_lose_draw()
            if end_of_game == True:
                quit()
                break
            random_choice()
            win_lose_draw()
            if end_of_game == True:
                quit()
                break
        else:
            screen_text.setText("You cannot click the filled squares!")

    #   2
    elif 0 < x < 100 < y < 200:
        screen_text.setText("")
        if text2 not in general_list:
            text2.setText("X")
            text2.draw(win)
            general_list.append(text2)
            sequence.append("X")
            win_lose_draw()
            if end_of_game == True:
                quit()
                break
            random_choice()
            win_lose_draw()
            if end_of_game == True:
                quit()
                break
        else:
            screen_text.setText("You cannot click the filled squares!")

    #   3
    elif 0 < x < 100 and 200 < y < 300:
        screen_text.setText("")
        if text3 not in general_list:
            text3.setText("X")
            text3.draw(win)
            general_list.append(text3)
            sequence.append("X")
            win_lose_draw()
            if end_of_game == True:
                quit()
                break
            random_choice()
            win_lose_draw()
            if end_of_game == True:
                quit()
                break
        else:
            screen_text.setText("You cannot click the filled squares!")

    #   4
    elif 0 < y < 100 < x < 200:
        screen_text.setText("")
        if text4 not in general_list:
            text4.setText("X")
            text4.draw(win)
            general_list.append(text4)
            sequence.append("X")
            win_lose_draw()
            if end_of_game == True:
                quit()
                break
            random_choice()
            win_lose_draw()
            if end_of_game == True:
                quit()
                break
        else:
            screen_text.setText("You cannot click the filled squares!")

    #   5
    elif 100 < x < 200 and 100 < y < 200:
        screen_text.setText("")
        if text5 not in general_list:
            text5.setText("X")
            text5.draw(win)
            general_list.append(text5)
            sequence.append("X")
            win_lose_draw()
            if end_of_game == True:
                quit()
                break
            random_choice()
            win_lose_draw()
            if end_of_game == True:
                quit()
                break
        else:
            screen_text.setText("You cannot click the filled squares!")

    #   6
    elif 100 < x < 200 < y < 300:
        screen_text.setText("")
        if text6 not in general_list:
            text6.setText("X")
            text6.draw(win)
            general_list.append(text6)
            sequence.append("X")
            win_lose_draw()
            if end_of_game == True:
                quit()
                break
            random_choice()
            win_lose_draw()
            if end_of_game == True:
                quit()
                break
        else:
            screen_text.setText("You cannot click the filled squares!")

    #   7
    elif 200 < x < 300 and 0 < y < 100:
        screen_text.setText("")
        if text7 not in general_list:
            text7.setText("X")
            text7.draw(win)
            general_list.append(text7)
            sequence.append("X")
            win_lose_draw()
            if end_of_game == True:
                quit()
                break
            random_choice()
            win_lose_draw()
            if end_of_game == True:
                quit()
                break
        else:
            screen_text.setText("You cannot click the filled squares!")

    #   8
    elif 100 < y < 200 < x < 300:
        screen_text.setText("")
        if text8 not in general_list:
            text8.setText("X")
            text8.draw(win)
            general_list.append(text8)
            sequence.append("X")
            win_lose_draw()
            if end_of_game == True:
                quit()
                break
            random_choice()
            win_lose_draw()
            if end_of_game == True:
                quit()
                break
        else:
            screen_text.setText("You cannot click the filled squares!")

    #   9
    elif 200 < x < 300 and 200 < y < 300:
        screen_text.setText("")
        if text9 not in general_list:
            text9.setText("X")
            text9.draw(win)
            general_list.append(text9)
            sequence.append("X")
            win_lose_draw()
            if end_of_game == True:
                quit()
                break
            random_choice()
            win_lose_draw()
            if end_of_game == True:
                quit()
                break
        else:
            screen_text.setText("You cannot click the filled squares!")
