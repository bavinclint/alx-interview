#!/usr/bin/python3
"""
A fuction that determines if the boxes can be opened
"""


def canUnlockAll(boxes):
    """ determine if it will open the boxes """
    boxNum = len(boxes)
    listNum = [0]
    for i in listNum:
        for n in boxes[i]:
            if n not in listNum:
                if n < boxNum:
                    myList.append(n)
    if len(listNum) == boxNum:
        return True
    return False
