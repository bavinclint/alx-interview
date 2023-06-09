#!/usr/bin/python3
"""
A fuction that determines if the boxes can be opened
"""


def canUnlockAll(boxes):
    """ determine if it will open the boxes """
    visited = [False for i in range(len(boxes))]
    visited[0] = True
    stack = [0]
    while len(stack):
        box = stack.pop(0)
        for _box in boxes[box]:
            if isinstance(_box, int) and _box >= 0 and _box < len(boxes)\
              and not visited[_box]:
                visited[_box] = True
                stack.append(_box)
    return all(visited)
