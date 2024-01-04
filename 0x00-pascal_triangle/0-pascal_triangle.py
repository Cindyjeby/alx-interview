#!/usr/bin/python3
"""
define class pascal triangle
"""

def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]
    for _ in range(1, n):
        prev_row = triangle[-1]
        new_row = [1] + [prev_row[i] + prev_row[i + 1] for i in range(len(prev_row) - 1)] + [1]
        triangle.append(new_row)

    return triangle
# Test the function
n = 5
result = pascal_triangle(n)
for row in result:
    print(row)
