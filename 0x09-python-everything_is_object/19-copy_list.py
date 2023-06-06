#!/usr/bin/python3
def copy_list(lst): return lst.copy() if hasattr(lst, 'copy') else list(lst)
