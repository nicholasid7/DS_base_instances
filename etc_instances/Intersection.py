# Instance 1: Intersections of sets
import numpy as np
import time as t

# a = [1, 2, 4, 6, 8, 10, 12]
# b = [0, 2, 3, 4, 8, 11, 13, 15, 17]

bound = 10000
a = [x for x in range(1, bound, 1)]
b = [x for x in range(11, bound, 2)]


# result [2,4,8]

#### Initial method #####
# O(n)
ts = t.time()
c = []
for i in a:
    for j in b:
        c.append(i) if i == j else 0
te = t.time()
t_0 = te-ts
print('exec_time_0->{}'.format(t_0))
print('c -> {}'.format(c[0:19]))

# O(n)-delta_x
#### Imporove 1 method #####
# a = [1, 2, 4, 6, 8, 10, 12]
# b = [0, 2, 3, 4, 8, 11, 13, 15, 17]
a = [x for x in range(1, bound, 1)]
b = [x for x in range(11, bound, 2)]

def b_similar(i_p, b):
    for i in range(len(b)):
        # for j in b:
        c_point = int(np.floor(len(b)/2))
        b_split = b[0:c_point] if i_p <= max(b[:c_point]) else b[c_point:]
        b = b_split
        if len(b) == 1:
            # print('b_split -> {}'.format(b_split))
            break
        # else:
        #     print('b_split -> {}'.format(b_split))
    return b_split[0]

ts = t.time()
c = []
for i_p in a:
    # print('-----')
    # print('i_p-{}'.format(i_p))
    b_s = b_similar(i_p, b)
    # print(b_s)
    # print(a)
    c.append(b_s) if b_s == i_p else 0#a.remove(i_p)
    # print('c->{}'.format(c))
te = t.time()
t_1 = te-ts
print('exec_time_ext->{}'.format(t_1))
print('c -> {}'.format(c[0:19]))

print('Estim t_1 vs t_0 -> {}'.format(t_0/t_1))


#### Imporove 2 method #####
# a = [1, 2, 4, 6, 8, 10, 12]
# b = [0, 2, 3, 4, 8, 11, 13, 15, 17]
a = [x for x in range(1, bound, 1)]
b = [x for x in range(11, bound, 2)]

max_min_ab = max(min(a), min(b))
min_max_ab = min(max(a), max(b))
# print(max_min_ab)
# print(min_max_ab)

# print(a.index(max_min_ab))
# print(a.index(min_max_ab))
# print(b.index(max_min_ab))
# print(b.index(min_max_ab))
# print('-----')

# print(a[::-1]) # reverse

# map_fltr = map(lambda x: x>5, a)
# print(list(map_fltr))


ts = t.time()
a_fltr = list(filter(lambda x: (x>=max_min_ab)&(x<=min_max_ab), a))
b_fltr = list(filter(lambda x: (x>=max_min_ab)&(x<=min_max_ab), b))
# print('a_fltr -> {}'.format(a_fltr))
# print('b_fltr -> {}'.format(b_fltr))

a = a_fltr
b = b_fltr

c = []
for i_p in a:
    # print('-----')
    # print('i_p-{}'.format(i_p))
    b_s = b_similar(i_p, b)
    # print(b_s)
    # print(a)
    c.append(b_s) if b_s == i_p else 0#a.remove(i_p)
    # print('c->{}'.format(c))
te = t.time()
t_2 = te-ts
print('exec_time_ext->{}'.format(t_2))
print('c -> {}'.format(c[0:19]))

print('Estim t_2 vs t_0 -> {}'.format(t_0/t_2))

