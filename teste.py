#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os



if __name__ == '__main__':
    pathtest = os.path.dirname(__file__)
    pathtest1 = os.path.join(pathtest, "analise")
    pathdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print (pathtest1)