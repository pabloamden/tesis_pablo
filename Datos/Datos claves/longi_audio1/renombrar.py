#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 15:21:22 2019

@author: leandro
"""

import os
from glob import glob

for f in glob("./*cha"):
    lst = f.split("-")
    newName = "./{}-{}-{}.cha".format(lst[1].lower(), "a1", lst[2])
    os.rename(f, newName)
