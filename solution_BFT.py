from collections import deque

def is_valid(maze, x, y):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0

def hasPath(maze, start, destination):
    if start == destination:
        return True
    queue = deque([start])
    visited = set()
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while queue:
        x, y = queue.popleft()
        visited.add((x, y))
        for dx, dy in directions:
            nx, ny = x, y
            while is_valid(maze, nx + dx, ny + dy):
                nx += dx
                ny += dy
            if (nx, ny) not in visited:
                queue.append((nx, ny))
                if [nx, ny] == destination:
                    return True
    return False