from dataclasses import replace
import queue


string = 'add 19 and 20'
q = string.replace("add", "")
q = q.replace("and", "")
print(q)
n1 = int(q.split()[0])
n2 = int(q.split()[1])
ans = n1 + n2
print(ans)