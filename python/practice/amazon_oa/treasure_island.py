# https://leetcode.com/discuss/interview-question/347457
# https://leetcode.com/discuss/interview-question/356150


def get_distance(grid, multi_source=False):
    m = len(grid)
    n = len(grid[0])
    if not m or not n or grid[0][0] == 'D':
        return -1
    if grid[0][0] == 'X':
        return 0

    # do bfs
    distance = 0
    queue = []
    if multi_source:
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'S':
                    queue.append((i, j, distance))
                    grid[i][j] = 'D'
    else:
        queue = [(0, 0, distance)]

    neighbors = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    while queue:
        i, j, distance = queue.pop(0)
        if grid[i][j] == 'X':
            return distance

        grid[i][j] = 'D'  # visited

        for i1, j1 in neighbors:
            boundary_conditions = 0 <= i + i1 < m and 0 <= j + j1 < n
            if not boundary_conditions or grid[i+i1][j+j1] == 'D':
                continue
            queue.append((i+i1, j+j1, distance+1))

    return -1


if __name__ == '__main__':
    treasure_map = [
        ['O', 'O', 'O', 'X'],
        ['O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O']
    ]
    print get_distance(treasure_map)

    treasure_map = [
        ['O', 'O', 'O', 'O'],
        ['D', 'O', 'D', 'O'],
        ['O', 'O', 'O', 'O'],
        ['X', 'D', 'D', 'O']
    ]
    print get_distance(treasure_map)

    treasure_map = [
        ['S', 'O', 'O', 'S', 'S'],
        ['D', 'O', 'D', 'O', 'D'],
        ['O', 'O', 'O', 'O', 'X'],
        ['X', 'D', 'D', 'O', 'O'],
        ['X', 'D', 'D', 'D', 'O']
    ]
    print get_distance(treasure_map, multi_source=True)

    treasure_map = [
        ['S', 'O', 'O', 'S', 'S'],
        ['D', 'O', 'D', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'X'],
        ['X', 'D', 'D', 'O', 'O'],
        ['X', 'D', 'D', 'D', 'O']
    ]
    print get_distance(treasure_map, multi_source=True)
