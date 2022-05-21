from tkinter import Label, Canvas, Tk
from random import randint

game_list = [[0] * 10 for i in range(10)]
spLab = []


def circle_check(x_coord, y_coord):
    if 0 <= x_coord < 10 and 0 <= y_coord < 10:
        global game_list
        if game_list[x_coord][y_coord] == 0 or game_list[x_coord][y_coord] == -1 or game_list[x_coord][y_coord] == -2:
            return True
        return False
    return True


def check_points(x_coordinate, y_coordinate):
    global game_list
    if game_list[x_coordinate][y_coordinate] != 0:
        return False
    if not circle_check(x_coordinate + 1, y_coordinate):
        return False
    if not circle_check(x_coordinate + 1, y_coordinate - 1):
        return False
    if not circle_check(x_coordinate + 1, y_coordinate + 1):
        return False
    if not circle_check(x_coordinate, y_coordinate + 1):
        return False
    if not circle_check(x_coordinate, y_coordinate - 1):
        return False
    if not circle_check(x_coordinate - 1, y_coordinate):
        return False
    if not circle_check(x_coordinate - 1, y_coordinate + 1):
        return False
    if not circle_check(x_coordinate - 1, y_coordinate - 1):
        return False
    return True


def set_coordinate1(x_coordinate, y_coordinate, count_deck, direction):
    global game_list
    if check_points(x_coordinate, y_coordinate):
        game_list[x_coordinate][y_coordinate] = 1
        if count_deck == 4:
            if direction == 0:
                game_list[x_coordinate - 1][y_coordinate] = 1
                game_list[x_coordinate - 2][y_coordinate] = 1
            elif direction == 1:
                game_list[x_coordinate + 1][y_coordinate] = 1
                game_list[x_coordinate + 2][y_coordinate] = 1
            elif direction == 2:
                game_list[x_coordinate][y_coordinate - 1] = 1
                game_list[x_coordinate][y_coordinate - 2] = 1
            else:
                game_list[x_coordinate][y_coordinate + 1] = 1
                game_list[x_coordinate][y_coordinate + 2] = 1
        if count_deck == 3:
            if direction == 0:
                game_list[x_coordinate - 1][y_coordinate] = 1
            elif direction == 1:
                game_list[x_coordinate + 1][y_coordinate] = 1
            elif direction == 2:
                game_list[x_coordinate][y_coordinate - 1] = 1
            else:
                game_list[x_coordinate][y_coordinate + 1] = 1
        return True
    return False


def set_last_deck(x_coordinate, y_coordinate, count):
    if count == 4:
        for direction in range(4):
            if direction == 0:
                x_coordinate = x_coordinate + 3
            elif direction == 1:
                x_coordinate = x_coordinate - 3
            elif direction == 2:
                y_coordinate = y_coordinate + 3
            else:
                y_coordinate = y_coordinate - 3
            if 0 <= x_coordinate < 10 and 0 <= y_coordinate < 10:
                if set_coordinate1(x_coordinate, y_coordinate, 4, direction):
                    return True
        return False
    if count == 3:
        for direction in range(4):
            if direction == 0:
                x_coordinate = x_coordinate + 2
            elif direction == 1:
                x_coordinate = x_coordinate - 2
            elif direction == 2:
                y_coordinate = y_coordinate + 2
            else:
                y_coordinate = y_coordinate - 2
            if 0 <= x_coordinate < 10 and 0 <= y_coordinate < 10:
                if set_coordinate1(x_coordinate, y_coordinate, 3, direction):
                    return True
            if direction == 0:
                x_coordinate = x_coordinate - 2
            elif direction == 1:
                x_coordinate = x_coordinate + 2
            elif direction == 2:
                y_coordinate = y_coordinate - 2
            else:
                y_coordinate = y_coordinate + 2
        return False
    if count == 2:
        for direction in range(4):
            if direction == 0:
                x_coordinate = x_coordinate + 1
            elif direction == 1:
                x_coordinate = x_coordinate - 1
            elif direction == 2:
                y_coordinate = y_coordinate + 1
            else:
                y_coordinate = y_coordinate - 1
            if 0 <= x_coordinate < 10 and 0 <= y_coordinate < 10:
                if set_coordinate1(x_coordinate, y_coordinate, 2, direction):
                    return True
            if direction == 0:
                x_coordinate = x_coordinate - 1
            elif direction == 1:
                x_coordinate = x_coordinate + 1
            elif direction == 2:
                y_coordinate = y_coordinate - 1
            else:
                y_coordinate = y_coordinate + 1
        return False


def make_1_deck():
    for i in range(4):
        while True:
            x_coord = randint(0, 9)
            y_coord = randint(0, 9)
            if set_coordinate1(x_coord, y_coord, 1, -1):
                break


def make_4_deck():
    while True:
        x_coord = randint(0, 9)
        y_coord = randint(0, 9)
        if set_coordinate1(x_coord, y_coord, 1, -1):
            if set_last_deck(x_coord, y_coord, 4):
                break
            game_list[x_coord][y_coord] = 0


def make_2_deck():
    for i in range(3):
        while True:
            x_coord = randint(0, 9)
            y_coord = randint(0, 9)
            if set_coordinate1(x_coord, y_coord, 1, -1):
                game_list[x_coord][y_coord] = 0
                if set_last_deck(x_coord, y_coord, 2):
                    game_list[x_coord][y_coord] = 1
                    break


def make_3_deck():
    for i in range(2):
        while True:
            x_coord = randint(0, 9)
            y_coord = randint(0, 9)
            if set_coordinate1(x_coord, y_coord, 1, -1):
                game_list[x_coord][y_coord] = 0
                if set_last_deck(x_coord, y_coord, 3):
                    game_list[x_coord][y_coord] = 1
                    break


window = Tk()
window.title("One-sided sea battle")
window.geometry("800x800")

canvas = Canvas(window, width=800, height=800)
canvas.grid()
for x in range(10):
    for y in range(10):
        canvas.create_rectangle((x + 1) * 60, (y + 1) * 60, (x + 2) * 60, (y + 2) * 60)

label1 = Label(
    text="A             B             C             D            E             F             G            H           "
         " I             J")
label1.place(x=80, y=30)

label2 = Label(
    text='1\n\n\n2\n\n\n3\n\n\n4\n\n\n5\n\n\n6\n\n\n7\n\n\n8\n\n\n9\n\n\n10')
label2.place(x=30, y=80)
make_1_deck()
make_4_deck()
make_2_deck()
make_3_deck()


def circle_check2(x_coord, y_coord):
    if 0 <= x_coord < 10 and 0 <= y_coord < 10:
        return True


def circle_check3(x_coord, y_coord):
    if 0 <= x_coord < 10 and 0 <= y_coord < 10:
        if game_list[x_coord][y_coord] == 0 or game_list[x_coord][y_coord] == -1:
            return True
        elif game_list[x_coord][y_coord] == -2:
            game_list[x_coord][y_coord] = -3
            return False
        return False
    return True


def check_last_deck(x_coord, y_coord):
    if not circle_check3(x_coord + 1, y_coord):
        if game_list[x_coord + 1][y_coord] == -3:
            game_list[x_coord][y_coord] = 0
            if not check_last_deck(x_coord + 1, y_coord):
                game_list[x_coord][y_coord] = -2
                game_list[x_coord + 1][y_coord] = -2
                return False
            game_list[x_coord][y_coord] = -2
            game_list[x_coord + 1][y_coord] = -2
        else:
            return False
    if not circle_check3(x_coord + 1, y_coord - 1):
        if game_list[x_coord + 1][y_coord - 1] == -3:
            game_list[x_coord][y_coord] = 0
            if not check_last_deck(x_coord + 1, y_coord - 1):
                game_list[x_coord][y_coord] = -2
                game_list[x_coord + 1][y_coord - 1] = -2
                return False
            game_list[x_coord][y_coord] = -2
            game_list[x_coord + 1][y_coord - 1] = -2
        else:
            return False
    if not circle_check3(x_coord + 1, y_coord + 1):
        if game_list[x_coord + 1][y_coord + 1] == -3:
            game_list[x_coord][y_coord] = 0
            if not check_last_deck(x_coord + 1, y_coord + 1):
                game_list[x_coord][y_coord] = -2
                game_list[x_coord + 1][y_coord + 1] = -2
                return False
            game_list[x_coord][y_coord] = -2
            game_list[x_coord + 1][y_coord + 1] = -2
        else:
            return False
    if not circle_check3(x_coord, y_coord + 1):
        if game_list[x_coord][y_coord + 1] == -3:
            game_list[x_coord][y_coord] = 0
            if not check_last_deck(x_coord, y_coord + 1):
                game_list[x_coord][y_coord] = -2
                game_list[x_coord][y_coord + 1] = -2
                return False
            game_list[x_coord][y_coord] = -2
            game_list[x_coord][y_coord + 1] = -2
        else:
            return False
    if not circle_check3(x_coord, y_coord - 1):
        if game_list[x_coord][y_coord - 1] == -3:
            game_list[x_coord][y_coord] = 0
            if not check_last_deck(x_coord, y_coord - 1):
                game_list[x_coord][y_coord] = -2
                game_list[x_coord][y_coord - 1] = -2
                return False
            game_list[x_coord][y_coord] = -2
            game_list[x_coord][y_coord - 1] = -2
        else:
            return False
    if not circle_check3(x_coord - 1, y_coord):
        if game_list[x_coord - 1][y_coord] == -3:
            game_list[x_coord][y_coord] = 0
            if not check_last_deck(x_coord - 1, y_coord):
                game_list[x_coord][y_coord] = -2
                game_list[x_coord - 1][y_coord] = -2
                return False
            game_list[x_coord][y_coord] = -2
            game_list[x_coord - 1][y_coord] = -2
        else:
            return False
    if not circle_check3(x_coord - 1, y_coord + 1):
        if game_list[x_coord - 1][y_coord + 1] == -3:
            game_list[x_coord][y_coord] = 0
            if not check_last_deck(x_coord - 1, y_coord + 1):
                game_list[x_coord][y_coord] = -2
                game_list[x_coord - 1][y_coord + 1] = -2
                return False
            game_list[x_coord][y_coord] = -2
            game_list[x_coord - 1][y_coord + 1] = -2
        else:
            return False
    if not circle_check3(x_coord - 1, y_coord - 1):
        if game_list[x_coord - 1][y_coord - 1] == -3:
            game_list[x_coord][y_coord] = 0
            if not check_last_deck(x_coord - 1, y_coord - 1):
                game_list[x_coord][y_coord] = -2
                game_list[x_coord - 1][y_coord - 1] = -2
                return False
            game_list[x_coord][y_coord] = -2
            game_list[x_coord - 1][y_coord - 1] = -2
        else:
            return False
    return True


def set_point(x_coord, y_coord):
    global game_list
    if circle_check2(x_coord + 1, y_coord):
        if game_list[x_coord + 1][y_coord] != -2:
            canvas.create_text((x_coord + 1) * 60 + 90, y_coord * 60 + 90, text='●')
            game_list[x_coord + 1][y_coord] = -1
    if circle_check2(x_coord - 1, y_coord):
        if game_list[x_coord - 1][y_coord] != -2:
            canvas.create_text((x_coord - 1) * 60 + 90, y_coord * 60 + 90, text='●')
            game_list[x_coord - 1][y_coord] = -1
    if circle_check2(x_coord, y_coord + 1):
        if game_list[x_coord][y_coord + 1] != -2:
            canvas.create_text(x_coord * 60 + 90, (y_coord + 1) * 60 + 90, text='●')
            game_list[x_coord][y_coord + 1] = -1
    if circle_check2(x_coord, y_coord - 1):
        if game_list[x_coord][y_coord - 1] != -2:
            canvas.create_text(x_coord * 60 + 90, (y_coord - 1) * 60 + 90, text='●')
            game_list[x_coord][y_coord - 1] = -1
    if circle_check2(x_coord + 1, y_coord + 1):
        if game_list[x_coord + 1][y_coord + 1] != -2:
            canvas.create_text((x_coord + 1) * 60 + 90, (y_coord + 1) * 60 + 90, text='●')
            game_list[x_coord + 1][y_coord + 1] = -1
    if circle_check2(x_coord - 1, y_coord - 1):
        if game_list[x_coord - 1][y_coord - 1] != -2:
            canvas.create_text((x_coord - 1) * 60 + 90, (y_coord - 1) * 60 + 90, text='●')
            game_list[x_coord - 1][y_coord - 1] = -1
    if circle_check2(x_coord + 1, y_coord - 1):
        if game_list[x_coord + 1][y_coord - 1] != -2:
            canvas.create_text((x_coord + 1) * 60 + 90, (y_coord - 1) * 60 + 90, text='●')
            game_list[x_coord + 1][y_coord - 1] = -1
    if circle_check2(x_coord - 1, y_coord + 1):
        if game_list[x_coord - 1][y_coord + 1] != -2:
            canvas.create_text((x_coord - 1) * 60 + 90, (y_coord + 1) * 60 + 90, text='●')
            game_list[x_coord - 1][y_coord + 1] = -1


def click(event):
    global game_list
    k = 0
    getx = event.x
    gety = event.y
    if 60 <= getx <= 660 and 60 <= gety <= 660:
        nx = int((getx-60)/60)
        ny = int((gety-60)/60)
        if game_list[nx][ny] == 0:
            canvas.create_text(nx * 60 + 90, ny * 60 + 90, text='●')
            game_list[nx][ny] = -1
        elif game_list[nx][ny] == 1:
            canvas.create_line(nx * 60 + 60, ny * 60 + 60, nx * 60 + 120, ny * 60 + 120)
            canvas.create_line(nx * 60 + 120, ny * 60 + 60, nx * 60 + 60, ny * 60 + 120)
            game_list[nx][ny] = -2
            if check_last_deck(nx, ny):
                for i in range(len(game_list)):
                    for j in range(len(game_list)):
                        if game_list[i][j] == -2:
                            set_point(i, j)
    for i in range(len(game_list)):
        for j in range(len(game_list)):
            if game_list[i][j] == 1:
                k += 1
    if k == 0:
        canvas.create_text(370, 370, text='You won!', font='Verdana 24')


window.bind('<Button-1>', click)

window.mainloop()
