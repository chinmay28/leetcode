# https://leetcode.com/discuss/interview-question/411357/


def get_infection_time(grid):
    queue = []  # triplet list of row, column and hours

    # this n^2 code just to find out the starting points
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                queue.append((i, j, 0))

    hours = 0
    while queue:
        i, j, hours = queue.pop(0)

        for i1, j1 in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            if 0 <= i + i1 < len(grid) and 0 <= j + j1 < len(grid[i]):

                if grid[i + i1][j + j1] == 0:
                    grid[i + i1][j + j1] = 1
                    queue.append((i + i1, j + j1, hours + 1))

    if any(0 in row for row in grid):
        return -1

    return hours
