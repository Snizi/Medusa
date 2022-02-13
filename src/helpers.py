from os import remove
import os
from re import I


def remove_empty_strings(domains):
    return [root for root in domains if root != ""]



def mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)
        return path
    else:
        return path

