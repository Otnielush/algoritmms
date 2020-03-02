# from environment.random_graph import *
from environment.random_map import *
from copy import copy,deepcopy


def h_func(x, y, tar_x, tar_y):
    return abs(tar_x-x)+abs(tar_y-y)


def f_func(graph, my_f, curr, point, end, diff=1):
    return my_f+(h_func(graph[curr][0], graph[curr][1], graph[point][0], graph[point][1])*diff)+h_func(graph[point][0], graph[point][1], graph[end][0], graph[end][1])

# graph - graph|map; map(bool) - if you send map
# graph[i][j]: i - number of point; j{0-2} - x and y position; j{2-...} - number of points linked point number
# map[i][j]=k: i and j - x,y position; k - type of cell(1=block)
def A_star(graph, start, goal, map=False):
    # convert map to graph
    if map:
        width = len(graph[0])
        height = len(graph)
        start = width*start[1]+start[0]
        goal = width*goal[1]+goal[0]
        new_graph = []
        xx = [-1, 0, 1, 0]
        yy = [0, -1, 0, 1]
        forest = []
        for y in range(height):

            for x in range(width):
                neibs = [x, y]

                for i in range(4):
                    if x + xx[i] < 0 or y + yy[i] < 0 or x + xx[i] >= width-1 or y + yy[i] >= height-1: continue
                    if graph[y + yy[i]][x + xx[i]] != 1:
                        neibs.append(width*(y + yy[i])+(x + xx[i]))
                # forest (cell value = 2) where cost of moving higher
                if graph[y][x] == 2:
                    forest.append(width*y+x)

                new_graph.append(neibs.copy())
        forest.sort()
        graph = deepcopy(new_graph)
        del(new_graph)

    # opens - checked cells
    opens = {}
    # cells that was there
    closed = []

    if start not in opens:
        opens_w = {start: [start]}
        opens = {start: h_func(graph[start][0], graph[start][1], graph[goal][0], graph[goal][1])}

    closed.append(start)
    # cell to where can go
    neibors = [x for x in graph[start][2:] if x not in closed]
    F = []
    for i in range(len(neibors)):
        if neibors[i] in forest:
            difficult = 1.5
        else:
            difficult = 1
        F.append(f_func(graph, opens[start], start, neibors[i], goal, difficult))
        # print("F: %d, my: %d, id: %d, neib id: %d, diff: %d" % (F[-1], opens[start], start, neibors[i], difficult))

    #  heuristic function for each possible move
    for i, neib in enumerate(neibors):
        # if point already calculated we checking m.b. new way is faster
        if neib in opens:
            if opens[neib] <= F[i]:
                opens[neib] = copy(F[i])
                opens_w[neib] = opens_w[start].copy()
                opens_w[neib].append(neib)
        else:
            opens[neib] = copy(F[i])
            opens_w[neib] = opens_w[start].copy()
            opens_w[neib].append(neib)

    opens.pop(start)
    opens_w.pop(start)

    while len(opens) > 0:
        # finding shortest checked point
        mini = min(opens, key=lambda x: opens[x])
        # print(opens[mini], "mini:", mini, opens_w[mini])

        if mini == goal:
            if map:
                new_way = []
                for open_w in opens_w[mini]:

                    xx = open_w%width
                    yy = open_w//width
                    new_way.append([xx, yy])
                return new_way, opens[mini]
            return opens_w[mini], opens[mini]

        closed.append(mini)

        neibors = [x for x in graph[mini][2:] if x not in closed]

        if len(neibors) > 0:
            F = []
            for i in range(len(neibors)):
                if neibors[i] in forest:
                    difficult = 1.5
                else:
                    difficult = 1
                F.append(f_func(graph, opens[mini], mini, neibors[i], goal, difficult))
                # print("F: %d, my: %d, id: %d, neib: %d, diff: %d"%(F[-1], opens[mini], mini, neibors[i], difficult))
            for i, neib in enumerate(neibors):
                if neib in opens:
                    if opens[neib] >= F[i]:
                        opens[neib] = copy(F[i])
                        opens_w[neib] = opens_w[mini].copy()
                        opens_w[neib].append(neib)
                else:
                    opens[neib] = copy(F[i])
                    opens_w[neib] = opens_w[mini].copy()
                    opens_w[neib].append(neib)

        opens.pop(mini)
        opens_w.pop(mini)
    return 0, 0


# GRAPH
# graph = build(14, 30, 3)
# for i,rr in enumerate(graph):
#     print(i,":",rr[0:2],"-",rr[2:])
# print_graph(graph, 30)

# pitaron = A_star(graph, 0, 4)
# print("way:", pitaron)



# MAP

# maps = build(30, 30, 12, 20)
maps =[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 2, 1, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 1], [1, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 2, 0, 0, 1, 1, 1], [1, 2, 2, 2, 2, 2, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 0, 2, 2, 0, 1, 1, 1, 1], [1, 1, 0, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 2, 2, 2, 0, 2, 0, 2, 0, 1, 1, 1, 1], [1, 0, 0, 0, 0, 2, 0, 0, 2, 2, 0, 0, 1, 2, 1, 1, 0, 0, 2, 1, 0, 2, 0, 0, 2, 0, 0, 0, 0, 1], [1, 0, 0, 0, 2, 2, 0, 2, 0, 2, 0, 0, 1, 1, 2, 2, 2, 1, 1, 1, 1, 0, 1, 0, 2, 2, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 2, 2, 0, 2, 2, 0, 0, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 2, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 2, 1, 2, 2, 2, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 1, 0, 0, 0, 0, 0, 2, 2, 2, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 0, 0, 0, 2, 2, 0, 2, 2, 0, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 2, 2, 0, 2, 0, 1], [1, 0, 1, 0, 0, 2, 2, 2, 0, 0, 2, 2, 0, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 2, 2, 2, 2, 0, 2, 1], [1, 1, 0, 0, 0, 0, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 0, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 0, 1], [1, 0, 0, 0, 0, 0, 2, 2, 2, 1, 1, 1, 1, 2, 0, 2, 2, 2, 0, 0, 1, 2, 2, 0, 0, 0, 2, 0, 0, 1], [1, 0, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 2, 0, 2, 2, 0, 0, 0, 0, 0, 0, 1], [1, 2, 2, 2, 0, 2, 2, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 2, 2, 0, 2, 1, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 2, 2, 2, 0, 2, 1, 1, 1, 0, 1, 1, 1, 0, 0, 2, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1], [1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
way, long = A_star(maps, [1,1], [25,28], map=True)
print_map(maps, way)
print(way)




