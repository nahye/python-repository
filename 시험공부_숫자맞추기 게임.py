import random

def make_question():
    a = random.randint(1,20)
    b = random.randint(1,10)
    op = random.randint(1,3)

    q = str(a)

    if op == 1:
        q=q+"+"
    if op == 2:
        q=q+"-"
    if op == 3:
        q=q+"*"

    q = q + str(b)

    return q

sc1 = 0
sc2 = 0

for x in range(5):
    q = make_question()
    print(q)
    
    ans = input("=")
    r = int(ans)

    if eval(q) == r:
        print("true")
        sc1 = sc1 + 1
    else:
        print("false")
        sc2 = sc2 + 1

print ("true:",sc1, "false:",sc2)

if sc2 == 0:
    print("good")
