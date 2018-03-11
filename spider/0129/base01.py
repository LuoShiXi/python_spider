#正则表达式

import re

##example01_[]中括号，匹配多种可能性
ptn = r"r[au]n"
print(re.search(ptn,"dog runs to cat"))

