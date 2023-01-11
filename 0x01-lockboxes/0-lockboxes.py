#!/usr/bin/python3
"""Module for task 0
"""


def canUnlockAll(boxes):
    """Function that determines if all the boxes are opened.

    Number of boxes is n.
    Each box is numbered sequentially from 0 to n - 1 and each box may
    contain keys to the other boxes.
    Key with the same number as a box opens that box.
    You can assume all keys will be positive integers.
    There can be keys that do not have boxes.
    The first box boxes[0] is unlocked.

    Args:
        boxes (List[List[int]]): list of lists of integers.

    Returns:
        boolean: True if all boxes can be unlocked, by using all the keys
        available in all the reachable boxes, and False otherwise.
    """
    # Initialize set of visited boxes, starting with the first box
    visited = {0}
    # Initialize queue with the first box
    queue = [boxes[0]]
    # While there are boxes in the queue
    # print("boxes type is {}".format(type(boxes)))
    while queue:
        # Take the first box from the queue
        box = queue.pop(0)
        # Iterate through the keys in the box
        for key in box:
            # If the key corresponds to a locked box that has not been
            # visited yet
            if key not in visited and key < len(boxes):
                # Mark the box as visited
                visited.add(key)
                # Add the box to the queue to explore its keys
                queue.append(boxes[key])
    # Return whether all boxes have been visited
    return len(visited) == len(boxes)
