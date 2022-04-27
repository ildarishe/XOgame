FLAG = True
field = [[0 for i in range(3)] for j in range(3)]

def draw_field():
    print("  1 2 3")
    for i in range(3):
        print(i + 1, end=" ")
        for j in range(3):
            if field[i][j] == -1:
                print("o", end=" ")
            elif field[i][j] == 1:
                print("x", end=" ")
            else:
                print(".", end=" ")
        print()

def correct_coords(x, y):
    if 1 <= x <= 3 and 1 <= y <= 3:
        if not field[x - 1][y - 1]:
            return True
        return False
    return False

def move(x, y):
    global FLAG
    if correct_coords(x, y):
        if FLAG:
            field[x-1][y-1] = 1
        else:
            field[x - 1][y - 1] = -1
        FLAG = not FLAG
        return True
    else:
        print("Неверный ход")
        return False

def check_for_win():
    if abs(field[0][0] + field[1][1] + field[2][2]) == 3:
        return True
    if abs(field[0][-1] + field[1][-2] + field[2][-3]) == 3:
        return True
    for i in range(0, 3):
        s = 0
        s1 = 0
        for j in range(0, 3):
            s += field[i][j]
            s1 += field[j][i]
        if abs(s) == 3 or abs(s1) == 3:
            print(s, s1)
            return True

def main():
    while not check_for_win():
        draw_field()
        if FLAG:
            print("Ход X -> ", end="")
        else:
            print("Ход O -> ", end="")
        x, y = [int(i) for i in input().split()]
        while not move(x, y):
            if FLAG:
                print("Ход X -> ", end="")
            else:
                print("Ход O -> ", end="")
            x, y = [int(i) for i in input().split()]
    draw_field()
    if not FLAG:
        print("Победил X!!!")
    else:
        print("Победил O!!!")


if __name__ == "__main__":
    main()