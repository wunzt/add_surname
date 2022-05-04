# Author: Thomas Wunz
# GitHub username: wunzt
# Date: 5/2/2022
# Description: Returns a list of names, from a larger list, that start with K and adds the surname Kardashian.
from typing import List

def add_surname(names):

    Kardashians = []

    for string in names:
        if string[0] == "K":
            Kardashians += [string + " Kardashian"]

    return Kardashians