from collections import deque

def shortest_path(rooms, doors, start, goal):
    """
    Compute one shortest path between start and goal in an undirected graph.

    Return:
      - list of room names from start to goal (inclusive),
      - [start] if start == goal,
      - [] if start/goal missing or no path exists.
    """

    # If no rooms or start/goal not in list → no path
    if not rooms or start not in rooms or goal not in rooms:
        return []

    # Special case: start == goal
    if start == goal:
        return [start]

    # Build adjacency list
    graph = {room: [] for room in rooms}
    for a, b in doors:
        if a in graph and b in graph:
            graph[a].append(b)
            graph[b].append(a)

    # BFS
    queue = deque([start])
    visited = {start}
    parent = {start: None}

    while queue:
        cur = queue.popleft()

        # Found goal → stop BFS
        if cur == goal:
            break

        for nxt in graph[cur]:
            if nxt not in visited:
                visited.add(nxt)
                parent[nxt] = cur
                queue.append(nxt)

    # If goal never reached
    if goal not in parent:
        return []

    # Reconstruct path backwards
    path = []
    cur = goal
    while cur is not None:
        path.append(cur)
        cur = parent[cur]

    path.reverse()
    return path


if __name__ == "__main__":
    rooms = ["Entrance", "Hall", "Gallery", "Cafe"]
    doors = [("Entrance", "Hall"), ("Hall", "Gallery"), ("Gallery", "Cafe")]
    print(shortest_path(rooms, doors, "Entrance", "Cafe"))
