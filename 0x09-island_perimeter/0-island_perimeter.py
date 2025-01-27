#!/usr/bin/python3
"""Module that calculates the perimeter of an island in a grid."""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.
    
    Args:
        grid (list of list of int): 2D grid where:
            - 0 represents water
            - 1 represents land
    
    Returns:
        int: Perimeter of the island
    """
    if not grid:
        return 0

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Add 4 for each land cell
                perimeter += 4
                
                # Check adjacent cells and subtract 2 for each adjacent land cell
                # Check cell above
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2
                # Check cell to the left
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2

    return perimeter