# https://docs.python.org/3/library/collections.html
# Collections
from collections import Counter
# Ini data
c = ['spam', 'egg', 'spam', 'green', 'counter', 'counter', 'counter', 'green', 'green', 'lake', 't','t']

c_c = Counter(c)
c_c_mc = c_c.most_common()[::-1]
print(c_c_mc)
print('Sorted')
print(
    sorted(c_c_mc, key=lambda x: x[::-1], reverse=False)
    # sorted(c_c_mc)
)

srt_res = sorted(c_c_mc, key=lambda x: x[::-1])
print('srt_res -> {}'.format(srt_res))
print('srt_res[0][0] -> {}'.format(srt_res[0][0]))

print('\n')
c = Counter(a=4, b=2, c=0, d=-2)
print(c)
print((c.most_common()[:-5:-1])) # lowest n-elements, i.e. -5
c += Counter() # remove elements less then 1 freq
print(c)

print('\n')
print(list(c.elements()))
print(list(c.items()))
print(dict(c))

print('\n')
print(Counter('abracadabra').most_common(3))


from collections import deque
print('\n')
print('----- deque -----')
c = deque(range(5), 7)
c.append(33)
c.appendleft(11)
c.appendleft(22)
# c.extendleft(range(5))
# c.pop()
# c.popleft()
c.remove(11)
# c.reverse()
c.rotate(-2)
print(c)

# always calls function
from collections import defaultdict
print('\n')
print('----- defaultdict -----')
defdict = defaultdict(list)
print(defdict)
for i in range(7):
    defdict[i].append(i)

print(defdict[2][0])

from collections import OrderedDict
print('\n')
print('----- defaultdict -----')

d = {'bb': 3, 'a':4, 'ppp': 1, 'o': 7}
print(d.items())
od_1 = OrderedDict(sorted(d.items(), key=lambda t: t[0]))
print(od_1)
od_2 = OrderedDict(sorted(d.items(), key=lambda t: t[1]))
print(od_2)
od_3 = OrderedDict(sorted(d.items(), key=lambda t: len(t[0])))
print(od_3)

from collections import namedtuple
print('\n')
print('----- namedtuple -----')
Point = namedtuple('Point_xy', ['x', 'y'])
p = Point(x=3, y=7)
print(p)
print(p.x)