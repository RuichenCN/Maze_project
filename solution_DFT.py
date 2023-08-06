def hasPath(maze, start, destination):
    def dfs(x, y):
        if [x, y] == destination:
            return True
        maze[x][y] = -1
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x, y
            while 0 <= nx + dx < len(maze) and 0 <= ny + dy < len(maze[0]) and maze[nx + dx][ny + dy] != 1:
                nx += dx
                ny += dy
            if maze[nx][ny] != -1 and dfs(nx, ny):
                return True
        return False
    return dfs(start[0], start[1])