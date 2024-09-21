#!/usr/bin/python3
"""
0-lockboxes module
Contains the canUnlockAll function that determines
if all boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Parameters:
    boxes (list of lists): A list where each index contains keys to other boxes.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False

    n = len(boxes)
    opened = [False] * n
    opened[0] = True  # The first box is unlocked by default
    keys = [0]  # Start with the key to the first box

    for key in keys:
        if isinstance(boxes[key], list):
            for k in boxes[key]:
                if isinstance(k, int) and 0 <= k < n and not opened[k]:
                    opened[k] = True
                    keys.append(k)

    return all(opened)

