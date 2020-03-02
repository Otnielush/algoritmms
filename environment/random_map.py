from random import randint


#  map[x][y]
# rocks - number of blocked cells
# forest - cells with higher move cost
def build(x, y, rocks, forests):
    map = [[0 for i in range(x)] for k in range(y)]
    x -= 1
    y -= 1
    # border
    for i in range(len(map)):
        map[i][0] = 1
        map[i][-1] = 1
    for i in range(len(map[0])):
        map[0][i] = 1
        map[-1][i] = 1

    for i in range(rocks):
        size_rock = randint(2, (x+y)/2)
        rock_x = randint(0, x)
        rock_y = randint(0, y)
        map[rock_x][rock_y] = 1
        for j in range(size_rock):
            x_min = 0 if rock_x-1 <= 0 else rock_x-1
            x_max = x if rock_x+1 >= x else rock_x+1
            y_min = 0 if rock_y-1 <= 0 else rock_y-1
            y_max = y if rock_y+1 >= y else rock_y+1
            # print("x", x_min, x_max, "y", y_min, y_max)
            rock_x = randint(x_min, x_max)
            rock_y = randint(y_min, y_max)
            # print("rand", rock_x, rock_y)
            map[rock_x][rock_y] = 1

    # print('---------------forest----------------')
    for i in range(forests):
        size_forest = randint(2, (x+y)/2)
        for_x = randint(1, x-1)
        for_y = randint(1, y-1)
        map[for_x][for_y] = 2
        for j in range(size_forest):
            x_min = 1 if for_x - 1 <= 1 else for_x - 1
            x_max = x-1 if for_x + 2 >= x else for_x + 1
            y_min = 1 if for_y - 1 <= 1 else for_y - 1
            y_max = y-1 if for_y + 2 >= y else for_y + 1
            # print("x", x_min, x_max, "y", y_min, y_max)
            for_x = randint(x_min, x_max)
            for_y = randint(y_min, y_max)
            # print("rand", for_x, for_y)
            map[for_x][for_y] = 2

    return map

def print_map(map, way=[]):
    if type(way) == list:
        if len(way) > 0:
            for point in way:
                if map[point[1]][point[0]] == 2 or map[point[1]][point[0]] == 19:
                    map[point[1]][point[0]] = 19
                else:
                    map[point[1]][point[0]] = 18

    decoder = {0:'   ', 1:'███', 2:'░░░', 10:'───',11:' │ ',12:' ┌─', 13:'─┐ ', 14:' └─', 15:'─┘ ', 16:' ∕ ', 17:' \ ', 18:' ○ ', 19:'░○░'}
    height = len(map)
    width = len(map[0])
    for x in range(height):
        print('|', end='')
        for y in range(width):
            print(decoder[map[x][y]], end='')
        print('|')
    print()




# dd = build(25, 25, 7, 2)
# way =[
#     [1,1],[1,2],[1,3],[2,3]
# ]
# print_map(dd, way)


