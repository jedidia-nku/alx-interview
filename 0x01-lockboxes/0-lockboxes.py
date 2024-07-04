#!/usr/bin/python3
"""
Module to determine if all boxes can be opened.
"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.
    
    Args:
        boxes (list of list of int): A list of lists where each list contains keys
                                     to other boxes.
    
    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    keys = boxes[0]

    for key in keys:
        if key < n and not opened[key]:
            opened[key] = True
            keys.extend(boxes[key])

    return all(opened)

# End of file with a newline character