TARGET = 361527

from math import sqrt, ceil


"""
n x n grid - odd, so 1 is center
m x m grid, - even, should convert to nxn


side = m
edge = additional numbers added by adding next square.
5x5, 17 - 25 are edge

"""
min_corner_size = ceil(sqrt(TARGET))
grid_val = min_corner_size**2
top_left = max_grid_val % 2 == 0

if top_left:
	grid_size = min_corner_size + 1
else:
	grid_size = min_corner_size

previous_max_grid_val = (grid_size - 1)**2

side_size = max_grid_val - previous_max_grid_val

corner = previous_max_grid_val + grid_size
first_midpoint = 

