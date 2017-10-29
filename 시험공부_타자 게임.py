import random
import time

w = ["cat", "dog", "fox", "panda", "snake"]
n=1
print("enter!")
input()
start = time.time()

q=random.choice(w)

while n<=5:
    print("question", n)
    print(q)
    x=input()

    if q==x:
        print("next!")
        n = n + 1
        q = random.choice(w)
    else:
        print("try again!")

end = time.time()
et = end - start
et = format(et, ".2f")
print("time:", et, "sec")
