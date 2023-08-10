import re

f = open("C://Users//benja//Documents//aptechWork//rstProject//join.src", "r")
y = ""
# match r"(= )\w+(()\w+();)"
for x in f:
    if re.search(r"= ", x):
        y = re.split(r"[=]", x)
        z = re.split(r"[(]", y[-1])
        break
title = z[0]
title = title.replace(" ", "")
print(title)