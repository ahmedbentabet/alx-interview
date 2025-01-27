#!/usr/bin/python3
"""Module that calculates the perimeter of an island."""


def island_perimeter(grid):
    """Calculate perimeter of island in grid.

    Args:
        grid (List[List[int]]): 2D list of 0's and 1's

    Returns:
        int: Perimeter of the island
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4

                # Check left neighbor
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2

                # Check upper neighbor
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2

    return perimeter
