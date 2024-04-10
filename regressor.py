import sys
import numpy as np

filename = sys.argv[1]
x = []
y = []
with open(filename, 'r') as f:
    for line in f.realines():