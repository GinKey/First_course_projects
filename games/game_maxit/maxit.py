# -*- coding: utf-8 -*-
import random
import os
import time

board = []  # список с числами
fist_player_points = 0  # очки первого игрока
second_player_points = 0  # очки второго игрока
win = 0  # определение победы
player_number = 1  # ход игрока
last_coord = 0  # предыдущая координата

# заполняем список рандомными элементами
for i in range(9):
    board.append(random.randint(1, 20))


# рисуем поле игры
def draw(board, fist_player_points, second_player_points):
    print()
    print("Игрок 1: " + str(fist_player_points) + " " * 13 + "Игрок 2: " + str(second_player_points))
    print()
    print(" " * 10 + "==============")
    for i in range(3):
        print(" " * 10 + "I", board[0 + i * 3], "I", board[1 + i * 3], "I", board[2 + i * 3], "I")
        print(" " * 10 + "==============")
    print()


# функция проверки нашего поля
def check_board(board):
    for i in range(len(board)):
        if board[i] != " ":
            return 1
    return 0


# функция хода игрока
def player_move(player_number, last_coord, board):
    check = []  # список элементов которые подходят, используется для проверки хода

    if last_coord == 0:  # первый ход, так как значение переменной 0
        print("Выберете номер клетки от 1 до 9:")
        check = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Ход: игрока", player_number)

    # если ход игрока 1
    if player_number == 1:

        print("Введите номер клетки в этой строке")
        if last_coord >= 1 and last_coord <= 3:

            if board[0] == " " and board[1] == " " and board[2] == " ":
                print("Вы не можете походить, ход переходит другому игроку")
                return "next_player"
            print("Вы можете выбрать только клетку от 1 до 3")
            check = [1, 2, 3]

        elif last_coord >= 4 and last_coord <= 6:
            if board[3] == " " and board[4] == " " and board[5] == " ":
                print("Вы не можете походить, ход переходит другому игроку")
                return "next_player"
            print("Вы можете выбрать только клетку от 4 до 6")
            check = [4, 5, 6]

        elif last_coord >= 7 and last_coord <= 9:
            if board[6] == " " and board[7] == " " and board[8] == " ":
                print("Вы не можете походить, ход переходит другому игроку")
                return "next_player"
            print("Вы можете выбрать только клетку от 7 до 9")
            check = [7, 8, 9]

    # иначе ход игрока 2
    else:
        print("Введите номер клетки в этом столбце")
        if last_coord == 1 or last_coord == 4 or last_coord == 7:
            if board[0] == " " and board[3] == " " and board[6] == " ":
                print("Вы не можете походить, ход переходит другому игроку")
                return "next_player"
            print("Вы можете выбрать только клетку 1 или 4 или 6")
            check = [1, 4, 7]
        elif last_coord == 2 or last_coord == 5 or last_coord == 8:
            if board[1] == " " and board[4] == " " and board[7] == " ":
                print("Вы не можете походить, ход переходит другому игроку")
                return "next_player"
            print("Вы можете выбрать только клетку 2 или 5 или 8")
            check = [2, 5, 8]
        elif last_coord == 3 or last_coord == 6 or last_coord == 9:
            if board[2] == " " and board[5] == " " and board[8] == " ":
                print("Вы не можете походить, ход переходит другому игроку")
                return "next_player"
            print("Вы можете выбрать только клетку 3 или 6 или 9")
            check = [3, 6, 9]

    coord = int(input())  # ввод нашей клетки
    # проверка на коррекстность ввода, пока мы не введем правильную клетку
    while coord not in check or last_coord == coord:
        if last_coord == coord:
            print("Вы не можете походить туда же.")
        print("Введите другой номер, этот не подходит")
        coord = int(input())
    return coord  # возвращаем значение


os.system('cls||clear')
while win != 1:  # пока игра не закончится
    if check_board(board) == 0:  # проверка если игра закончилась

        win = 1

        print()
        print("Счет: ")
        print("Игрок 1: " + str(fist_player_points) + " " * 13 + "Игрок 2: " + str(second_player_points))
        print()

        # определяем, кто победил
        if fist_player_points > second_player_points:
            print("победил игрок 1")
        elif second_player_points > fist_player_points:
            print("победил игрок 2")
        else:
            print("ничья")
        break

    draw(board, fist_player_points, second_player_points)  # рисуем поле
    coord = player_move(player_number, last_coord, board)

    if coord == "next_player":
        if player_number == 1:
            player_number = 2
        else:
            player_number = 1

        last_coord = 0
    else:
        if player_number == 1:
            fist_player_points += board[coord - 1]
            player_number = 2
        else:
            second_player_points += board[coord - 1]
            player_number = 1
        board[coord - 1] = " "
        last_coord = coord

    time.sleep(0.5)
    os.system('cls||clear')
