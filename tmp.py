import hashlib
import time


# print(hashlib.algorithms_guaranteed)

# h1 = hashlib.sha256()
# h1.update(b'du')
# print(h1.hexdigest())



with open('pan-tadeusz.txt', 'r', encoding="utf8") as pt:
    h1 = hashlib.sha256()
    h2 = hashlib.sha256()
    a = ''
    for line in pt:
        a += line
    start = time.time()
    a = a*1000
    h1.update(a.encode("utf-8"))
    print(h1.hexdigest())
    print(round((time.time() - start) * 1000, 2), 'ms')
