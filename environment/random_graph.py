from random import randint

# graph[num point][x, y]

def build(num, long, ways):
    points = [[randint(0, long-1), randint(0, long-1)] for x in range(num)]

    for i, point in enumerate(points):
        ways_h = [x for x in range(num)]
        ways_h.__delitem__(i)

        ways_n = randint(int(ways*0.2), int(ways*1.8))
        dells = num-ways_n-1
        for j in range(dells):
            to_del = len(ways_h)-1
            ways_h.__delitem__(randint(0, to_del))

        point.extend(ways_h)

    return points

def print_graph(graph, long):
    table = [['   ' for i in range(long)] for j in range(long)]
    for i, point in enumerate(graph):
        # точки
        table[point[1]][point[0]] = ' ' + str(i) + ' '

        # дорога
        for j in range(2, len(point)):
            way_y = graph[point[j]][1] - point[1]
            way_x = graph[point[j]][0] - point[0]
            step = max(abs(way_x), abs(way_y))
            step_m = 0 if abs(way_x) >= step else 1
            ratio = 0
            if step_m == 0:
                if way_x != 0:
                    sign = int(way_x/abs(way_x))
                    ratio = float(way_y) / way_x
                for k in range(abs(way_x)):
                    k *= sign
                    if table[round(k*ratio)+point[1]][k+point[0]] == '   ':
                        table[round(k*ratio)+point[1]][k+point[0]] = ' · '
            else:
                if way_y != 0:
                    sign = int(way_y/abs(way_y))
                    ratio = float(way_x) / way_y
                for k in range(abs(way_y)):
                    k *= sign
                    if table[k+point[1]][round(k*ratio)+point[0]] == '   ':
                        table[k+point[1]][round(k*ratio)+point[0]] = ' · '



    for j in range(len(table)):
        print('|', end='')
        for k in range(len(table[j])):
            print(table[j][k], end='')
        print('|\n', end='')


# xx = build(5, 40, 2)
# print(xx)
# print_graph(xx, 40)

