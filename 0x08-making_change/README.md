# Making Change

## Description
This project implements a solution to the coin change problem using dynamic programming. The goal is to determine the fewest number of coins needed to meet a given total amount.

## Requirements
- Python 3.4.3
- Ubuntu 20.04 LTS
- PEP 8 style guide (version 1.7.x)

## Function Prototype
```python
def makeChange(coins, total)
```

### Parameters
- `coins`: List of coin denominations (integers > 0)
- `total`: Target total amount

### Returns
- Fewest number of coins needed to meet the total
- `0` if total is 0 or less
- `-1` if total cannot be met by any combination of coins

## Example
```python
print(makeChange([1, 2, 25], 37))  # Output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
```

## Approach
Uses dynamic programming to efficiently calculate the minimum number of coins needed.
- Time Complexity: O(total * len(coins))
- Space Complexity: O(total)