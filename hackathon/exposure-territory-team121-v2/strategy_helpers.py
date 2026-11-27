"""Safety/territory helpers for team121 v2.

Use these helpers from the official player-kit adapter. The official engine remains
source of truth for movement, closure, and scoring; prefer game.copy().step()
for candidate validation when the SDK exposes it.
"""
from collections import deque

DIRS = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}
OPPOSITE = {"U": "D", "D": "U", "L": "R", "R": "L"}

def legal_commands(direction):
    """Return commands that don't request an illegal instant reversal."""
    return [c for c in DIRS if c != OPPOSITE.get(direction)]

def bfs_first_step(start, goal, passable):
    """Shortest path first command on a 4-neighbour grid; None if unreachable."""
    if start == goal:
        return None
    q = deque([start])
    parent = {start: None}
    first = {}
    while q:
        p = q.popleft()
        for cmd, (dx, dy) in DIRS.items():
            n = (p[0] + dx, p[1] + dy)
            if n in parent or not passable(*n):
                continue
            parent[n] = p
            first[n] = cmd if p == start else first[p]
            if n == goal:
                return first[n]
            q.append(n)
    return None

def territory_value(owner, terrain, me, base=None):
    """Raw owned-cell value; base/calibration cells can be excluded."""
    total = 0
    h = len(owner)
    w = len(owner[0]) if h else 0
    for y in range(h):
        for x in range(w):
            if owner[y][x] != me:
                continue
            if base is not None and base[y][x] >= 0:
                continue
            total += 3 if terrain[y][x] == "*" else 1
    return total

def exposed_edges(owner, me, base=None):
    """Count owned edges facing board edge, neutral, defect, or enemy."""
    h = len(owner)
    w = len(owner[0]) if h else 0
    count = 0
    for y in range(h):
        for x in range(w):
            if owner[y][x] != me or (base is not None and base[y][x] >= 0):
                continue
            for dx, dy in DIRS.values():
                nx, ny = x + dx, y + dy
                if not (0 <= nx < w and 0 <= ny < h) or owner[ny][nx] != me:
                    count += 1
    return count

def static_score(owner, terrain, me, base=None):
    """Score estimate matching the exposed-edge rule, for non-base cells."""
    return territory_value(owner, terrain, me, base) - exposed_edges(owner, me, base) // 3
