# Instance 1: Intersections of sets
import numpy as np

a = [1, 2, 4, 6, 8, 10, 12]
b = [2, 3, 4, 8]

# result [2,4,8]
max_min_ab = max(min(a), min(b))
min_max_ab = min(max(a), max(b))
print(max_min_ab)
print(min_max_ab)


