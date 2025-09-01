def minesweeper(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    # directions for 8 neighbors (vertical, horizontal, diagonal)
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    
    result = []
    for r in range(rows):
        row_result = []
        for c in range(cols):
            if grid[r][c] == "#":
                row_result.append("#")
            else:
                # count mines around
                count = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "#":
                        count += 1
                row_result.append(count)
        result.append(row_result)
    
    return result


# Example
grid = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"]
]


output = minesweeper(grid)
for row in output:
    print(row)
