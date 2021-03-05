from collections import Counter
# Ini data
c = ['spam', 'egg', 'spam', 'green', 'counter', 'counter', 'counter', 'green', 'green', 'lake']

c_c = Counter(c)
c_c_mc = c_c.most_common()#[::-1]
print(c_c_mc)
print(
    # c_c_mc.sort()
    sorted(c_c_mc, key=lambda x: x)
)

srt_res = sorted(c_c_mc, key=lambda x: x[::-1])[0][0]
print(srt_res)

# sorted(x, key=x.get, reverse=True)
# print(sorted(c_c, key=c_c))
# c_c_rev = c_c[::-1]
# print(c_c_rev)
