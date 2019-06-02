import numpy as np


def heuristic(i, g, algorithm_selector):
    dist = 0
    if algorithm_selector == 1:
        for x in range(0, 3):
            for y in range(0, 3):
                k = np.where(g == i[x][y])
                dist += abs(k[0] - x) + abs(k[1] - y)
        dist = dist[0]
    elif algorithm_selector == 2:
        dist += np.count_nonzero(g - i)
    elif algorithm_selector == 3:
        dist = heuristic(i, g, 1) + heuristic(i, g, 2)
    return dist


def change_state(a, g):
    algorithm_sel = 2
    loc = np.where(a == 0)
    x = [loc[0][0], loc[1][0]]
    up = [x[0], x[1]-1]
    down = [x[0], x[1]+1]
    left = [x[0]-1, x[1]]
    right = [x[0]+1, x[1]]
    moves = [up, down, left, right]
    temp_new_states = []
    dist = []
    new_states = []
    for i in moves:
        if 3 > i[0] >= 0 and 3 > i[1] >= 0:
            temp = a.copy()
            temp[i[0], i[1]], temp[x[0], x[1]] = temp[x[0], x[1]], temp[i[0], i[1]]
            temp_new_states.append(temp)
    for i in temp_new_states:
        dist.append(heuristic(i, g, algorithm_sel))
    for k in sorted(list(set(dist))):
        for i in temp_new_states:
            if heuristic(i, g, algorithm_sel) == k:
                new_states.append(i)
    return new_states


def check_visited(t, e):
    for i in e:
        if np.array_equal(t, i):
            return False
    return True


def get_index(i, new_states):
    for k in range(len(new_states)):
        if np.array_equal(i, new_states[k]):
            return k


def a_star(s, g):
    count = 0
    explored = []
    frontier = [s]
    while True:
        temp = frontier[0]
        frontier.remove(temp)
        count += 1
        print("Selected : ", temp, sep='\n')
        if np.array_equal(temp, g):
            print("Goal State Reached")
            break
        new_states = change_state(temp, g)
        for i in new_states:
            if check_visited(i, explored):
                frontier.insert(get_index(i, new_states), i)
                # frontier.append(i)
                print("Added : ")
                print(i)
        explored.append(temp)
        print(end='\n\n')
    print(count)


start = np.array([[4, 1, 3], [0, 2, 5], [7, 8, 6]])
goal = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
a_star(start, goal)
