# Generator instances
# DIf fltr
list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
list_b = [x for x in list_a]

print(list_a)
print(list_b)
print(list_a is list_b)


list_b = [x for x in list_a if x % 2 == 0 and x > 0]
print(list_b)

list_b = [x**2 for x in list_a]
print(list_b)


list_b = [x if x < 0 else x**2 for x in list_a]
print(list_b)

list_b = [x**3 if x < 0 else x**2 for x in list_a if x % 2 == 0]
print(list_b)

numbers = range(10)
squared_evens = [
    n ** 2
    for n in numbers
    if n % 2 == 0
]
print(squared_evens)

##### 1 Gen list #####
numbers = range(10)
squared_evens = [n ** 2 for n in numbers if n % 2 == 0]
print(squared_evens)

##### 2 For #####
numbers = range(10)
squared_evens = []
for n in numbers:
    if n % 2 == 0:
        squared_evens.append(n ** 2)
print(squared_evens)

##### 3 funct #####
numbers = range(10)
squared_evens = map(lambda n: n ** 2, filter(lambda n: n % 2 == 0, numbers))
print(list(squared_evens))

##### 4 Gen expr - opt memory use #####
list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
my_gen = (i for i in list_a) # write only with brackets; len() & print() & my_gen[1:3] don't work;
print(next(my_gen))
print(next(my_gen))

my_sum = sum(i for i in list_a)
print(my_sum)
# print(next(my_sum)) #error - not an iterator

my_gen = (i for i in list_a)
print(sum(my_gen))  # 12
print(sum(my_gen))  # 0

##### inf generator #####
import itertools
inf_gen = (x for x in itertools.count())

##### 5 Generate collections #####
# Collection generated all
# 11 Generator - List
list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
my_list = [i for i in list_a]
print(my_list)

# 22 Generator - Set
list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
my_set= {i for i in list_a}
print(my_set) # {0, 1, 2, 3, 4, 5, -1, -2} - порядок случаен

# 33 Generator - dict
dict_abc = {'a': 1, 'b': 2, 'c': 3, 'd': 3}
dict_123 = {v: k for k, v in dict_abc.items()}
print(dict_123)  # {1: 'a', 2: 'b', 3: 'd'}, c - except: because index 3 is similar for c&d, we use last - d

# Dict from List
list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
dict_a = {x: x**2 for x in list_a}
print(dict_a)

# dict_gen = (x: x**2 for x in list_a)      # SyntaxError: invalid syntax
dict_gen = ((x, x ** 2) for x in list_a)    # Корректный вариант генератора-выражения для словаря
print(dict_a)
# dict_a = dict(x: x**2 for x in list_a)    # SyntaxError: invalid syntax
dict_a = dict((x, x ** 2) for x in list_a)  # Корректный вариант синтаксиса от @longclaps
print(dict_a)

##### 6 Generate Str -> .join() #####
my_str = ''.join(str(x) for x in list_a)
print(my_str) # -2-1012345

##### 7 Periodic and pertial select #####
##### 7.1 Internal cycle #####   [expression for x in iter1 for y in iter2]
##### 7.1.1 #####
rows = 1, 2, 3
cols = 'a', 'b'
my_dict = {(col, row): 0 for row in rows for col in cols}
print(my_dict)  # {('a', 1): 0, ('b', 2): 0, ('b', 3): 0, ('b', 1): 0, ('a', 3): 0, ('a', 2): 0}

my_dict['b', 2] = 10   # задаем значение по координатному ключу-кортежу
print(my_dict['b', 2])   # 10 - получаем значение по координатному ключу-кортежу

# with fltr
rows = 1, 2, -3, -4, -5
cols = 'a', 'b', 'abc'
# Для наглядности разнесем на несколько строк
my_dict = {
    (col, row): 0  # каждый элемент состоит из ключа-кортежа и нулевого знаечния
    for row in rows if row > 0   # Только положительные значения
    for col in cols if len(col) == 1  # Только односимвольные
    }
print(my_dict)  # {('a', 1): 0, ('b', 2): 0, ('b', 3): 0, ('b', 1): 0, ('a', 3): 0, ('a', 2): 0}

##### 7.1.2 Internal cycle #####   Вложенные циклы for где внутренний цикл идет по результату внешнего цикла
#  [expression for x in iterator for y in x].
matrix = [[0, 1, 2, 3],
          [10, 11, 12, 13],
          [20, 21, 22, 23]]

# Решение с помощью генератора списка:
flattened = [n for row in matrix for n in row]
print(flattened)    # [0, 1, 2, 3, 10, 11, 12, 13, 20, 21, 22, 23]

# Таже задача, решенная с помощью вложенных циклов
flattened = []
for row in matrix:
    for n in row:
        flattened.append(n)
print(flattened)

# UPD:Изящные решения
import itertools
flattened = list(itertools.chain.from_iterable(matrix))
print(flattened)
# Данный подходнамного быстрее генератора списков
# и рекомендован к использованию для подобных задач.

flattened = sum(matrix, [])
print(flattened)
# sum(a, []) имеет квадратическую сложность(O(n^2))
# и потому совсем не рекомендуется к использованию для таких целей

##### 7.2 Internal Generators #####
# Для вложенных генераторов,
# вначале обрабатывается внешний генератор, потом внутренний,
# то есть порядок идет справа-налево.

##### 7.2.1 Вложенный генератор внутри генератора — двумерная из двух одномерных #####
#   [[expression for y in iter2] for x in iter1]
w, h = 5, 3  # зададим ширину и высотку матрицы
matrix = [[0 for x in range(w)] for y in range(h)]
print(matrix)   # [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

# Создание этой же матрицы двумя вложенными циклами - порядок вложения!!!
matrix = []
for y in range(h):
    new_row = []
    for x in range(w):
        new_row.append(0)
    matrix.append(new_row)
print(matrix)   # [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

##### 7.2.1 Вложенный генератор внутри генератора — двумерная из двумерной #####
#   [[expression for y in x] for x in iterator]
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
squared = [[cell**2 for cell in row] for row in matrix]
print(squared)    # [[1, 4, 9, 16], [25, 36, 49, 64], [81, 100, 121, 144]]

# Эта же операция в виде вложенных циклов
squared = []
for row in matrix:
    new_row = []
    for cell in row:
        new_row.append(cell**2)
    squared.append(new_row)
print(squared)    # [[1, 4, 9, 16], [25, 36, 49, 64], [81, 100, 121, 144]]

##### 7.3 Генератор итерирующийся по генератору #####
list_a = [x for x in range(-2, 4)]
list_b = [x**2 for x in list_a]
list_c = [x**2 for x in [x for x in range(-2, 4)]]
print(list_c)  # [4, 1, 0, 1, 4, 9]

# Преимущество от комбинирования генераторов на примере сложной функции f(x) = u(v(x))
list_c = [t + t ** 2  for t in (x ** 3 + x ** 4 for x in range(-2, 4))]
print(list_c)

print('\n')
##### 8 Use range #####
##### App 9 Additional instances #####

##### 9.1 Последовательный проход по нескольким спискам
import itertools
l1 = [1,2,3]
l2 = [10,20,30]
result = [l*1 for l in itertools.chain(l1, l2)]
print(result)   # [2, 4, 6, 20, 40, 60]

##### 9.2 Транспозиция матрицы
# (Преобразование матрицы, когда строки меняются местами со столбцами).
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed)  # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
print(len(matrix[0]))

# Эта же транспозиция матрицы в виде цикла
transposed = []
for i in range(len(matrix[0])):
    new_row = []
    for row in matrix:
        new_row.append(row[i])
    transposed.append(new_row)
print(transposed)  # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# Эта же транспозиция матрицы в другом виде
transposed = list(map(list, zip(*matrix)))
print(transposed)  # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

##### 9.3 Задача выбора только рабочих дней
print('\n')
# Формируем список дней от 1 до 31 с которым будем работать
days = [d for d in range(1, 32)]

# Делим список дней на недели
weeks = [days[i:i+7] for i in range(0, len(days), 7)]
print(weeks)   # [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21], [22, 23, 24, 25, 26, 27, 28], [29, 30, 31]]

# Выбираем в каждой неделе только первые 5 рабочих дней, отбрасывая остальные
work_weeks = [week[0:5] for week in weeks]
print(work_weeks)   # [[1, 2, 3, 4, 5], [8, 9, 10, 11, 12], [15, 16, 17, 18, 19], [22, 23, 24, 25, 26], [29, 30, 31]]

# Если нужно одним списком дней - можно объединить
wdays = [item for sublist in work_weeks for item in sublist]
print(wdays)   # [1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 15, 16, 17, 18, 19, 22, 23, 24, 25, 26, 29, 30, 31]


print('\n')
# Эта же решение в другом виде
# Формируем список дней от 1 до 31 с которым будем работать
days = [d for d in range(1, 32)]

wdays6 = [wd for (i, wd) in enumerate(days, 1) if i % 7 != 0]  # Удаляем каждый 7-й день
# Удаляем каждый 6 день в оставшихся после первого удаления:
wdays5 = [wd for (i, wd) in enumerate(wdays6, 1) if i % 6 != 0]

print(wdays5)
# [1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 15, 16, 17, 18, 19, 22, 23, 24, 25, 26, 29, 30, 31]

# Обратите внимание, что просто объединить два условия в одном if не получится,
# как минимум потому, что 12-й день делится на 6, но не выпадает на последний 2 дня недели!

# Best короткое решение:
days = [d + 1 for d in range(31) if d % 7 < 5]


##### App 10 Additional instances #####
