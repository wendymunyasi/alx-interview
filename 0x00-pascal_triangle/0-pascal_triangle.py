#!/usr/bin/python3
"""
function def pascal_triangle(n): that returns a list of lists of integers
representing the Pascal's triangle of n
"""


def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal's
    triangle of n

    Args:
        n (integer): number of rows

    Returns:
        list: integers representing Pascal's triangle.
    """
    # if n is less or 0 return an empty list
    if n <= 0:
        return []

    else:
        # Initialize a variable called triangle with a list containing a
        # single element, [1], which represents the first row of the triangle.
        triangle = [[1]]

        for i in range(1, n):
            # On each iteration of the loop, a new list is created and
            # appended to the triangle variable. This list starts with a
            # single element, 1, which represents the first element of the
            # new row.
            triangle.append([1])

            # The function then enters a nested loop that iterates over the
            # elements in the previous row (the row with an index of i-1) and
            # calculates the value of each element in the new row (the row
            # with an index of i) based on the sum of the elements in the
            # previous row that are directly above and to the left and right
            # of the current element.
            for j in range(1, i):
                triangle[i].append(triangle[i-1][j-1] + triangle[i-1][j])

            # This process continues until all of the elements in the new row
            # have been calculated, at which point a final 1 is appended to
            # the end of the row to complete it.
            triangle[i].append(1)
        return triangle
