
import os 

import sys
a="[]"
b="[]"
c="[]"
d="[]"
e="[]"
f="[]"
g="[]"
h="[]"
k="[]"
print("Начало игры")
print(a, b, c, "       [a]", "[b]", "[c]")
print(d, e, f, "       [d]", "[e]", "[f]")
print(g, h, k, "       [g]", "[h]", "[k]")
x1=input("Ход игрока 0:  ")
if x1=="a":
    a=" 0"
if x1=="b":
    b=" 0"
if x1=="c":
    c=" 0"
if x1=="d":
    d=" 0"
if x1=="e":
    e=" 0"
if x1=="f":
    f=" 0"
if x1=="g":
    g=" 0"
if x1=="h":
    h=" 0"
if x1=="k":
    k=" 0"
clear = lambda: os.system('cls')
clear()
print(a, b, c, "       [a]", "[b]", "[c]")
print(d, e, f, "       [d]", "[e]", "[f]")
print(g, h, k, "       [g]", "[h]", "[k]")
x2 = input("Ход игрока x:  ")
if x2 == x1:
    print("Так нельзя")
    x2 = input("Ход игрока x:  ")
if x2 == "a":
    a = " x"
if x2 == "b":
    b = " x"
if x2 == "c":
    c = " x"
if x2 == "d":
    d = " x"
if x2 == "e":
    e = " x"
if x2 == "f":
    f = " x"
if x2 == "g":
    g = " x"
if x2 == "h":
    h = " x"
if x2 == "k":
    k = " x"
clear = lambda: os.system('cls')
clear()
print(a, b, c, "       [a]", "[b]", "[c]")
print(d, e, f, "       [d]", "[e]", "[f]")
print(g, h, k, "       [g]", "[h]", "[k]")
x3 = input("Ход игрока 0:  ")
if x2 == x3 or x3 == x1:
    print("Так нельзя")
    x3 = input("Ход игрока x:  ")
if x3 == "a":
    a = " 0"
if x3 == "b":
    b = " 0"
if x3 == "c":
    c = " 0"
if x3 == "d":
    d = " 0"
if x3 == "e":
    e = " 0"
if x3 == "f":
    f = " 0"
if x3 == "g":
    g = " 0"
if x3 == "h":
    h = " 0"
if x3 == "k":
    k = " 0"
clear = lambda: os.system('cls')
clear()
print(a, b, c, "       [a]", "[b]", "[c]")
print(d, e, f, "       [d]", "[e]", "[f]")
print(g, h, k, "       [g]", "[h]", "[k]")
x4 = input("Ход игрока x:  ")
if x1 == x4 or x2 == x4 or x3 ==x4 :
    print("Так нельзя")
    x4 = input("Ход игрока x:  ")
if x4 == "a":
    a = " x"
if x4 == "b":
    b = " x"
if x4 == "c":
    c = " x"
if x4 == "d":
    d = " x"
if x4 == "e":
    e = " x"
if x4 == "f":
    f = " x"
if x4 == "g":
    g = " x"
if x4 == "h":
    h = " x"
if x4 == "k":
    k = " x"
clear = lambda: os.system('cls')
clear()
print(a, b, c, "       [a]", "[b]", "[c]")
print(d, e, f, "       [d]", "[e]", "[f]")
print(g, h, k, "       [g]", "[h]", "[k]")
x5 = input("Ход игрока 0:  ")
if x1 == x5 or x2 == x5 or x3 == x5 or x4 == x5:
    print("Так нельзя")
    x5 = input("Ход игрока 0:  ")
if x5 == "a":
    a = " 0"
if x5 == "b":
    b = " 0"
if x5 == "c":
    c = " 0"
if x5 == "d":
    d = " 0"
if x5 == "e":
    e = " 0"
if x5 == "f":
    f = " 0"
if x5 == "g":
    g = " 0"
if x5 == "h":
    h = " 0"
if x5 == "k":
    k = " 0"
if a==" x"  and b==" x" and c == " x" or c==" x" and f==" x" and k == " x" or g==" x" and h==" x" and k == " x" or a==" x" and d==" x" and g == " x" or a==" x" and e==" x" and k == " x" or g==" x" and e==" x" and c == " x"  or d==" x" and e ==" x" and f==" x" or b==" x" and e==" x" and h==" x":
    print("Выграл игрок X!!!")
    print("Выграл игрок X!!!")
    print("Выграл игрок X!!!")
    print(a, b, c)
    print(d, e, f)
    print(g, h, k)
    input('Press ENTER to exit')
    sys.exit()
if a==" 0" and b==" 0" and c == " 0" or c==" 0" and f==" 0" and k == " 0" or g==" 0" and h==" 0" and k == " 0" or a==" 0" and d==" 0" and g == " 0" or a==" 0" and e==" 0" and k == " 0" or g==" 0" and e==" 0" and c == " 0" or d==" 0" and e ==" 0" and f==" 0" or b==" 0" and e==" 0" and h==" 0":
    print("Выграл игрок 0!!!")
    print("Выграл игрок 0!!!")
    print("Выграл игрок 0!!!")
    print(a, b, c)
    print(d, e, f)
    print(g, h, k)
    input('Press ENTER to exit')
    sys.exit()
clear = lambda: os.system('cls')
clear()
print(a, b, c, "       [a]", "[b]", "[c]")
print(d, e, f, "       [d]", "[e]", "[f]")
print(g, h, k, "       [g]", "[h]", "[k]")  
x6 = input("Ход игрока x:  ")
if x1 == x6 or x2 == x6 or x3 ==x6 or x5 == x6 or x4 == x6 or x5 == x6:
    print("Так нельзя")
    x6 = input("Ход игрока x:  ")
if x6 == "a":
    a = " x"
if x6 == "b":
    b = " x"
if x6 == "c":
    c = " x"
if x6 == "d":
    d = " x"
if x6 == "e":
    e = " x"
if x6 == "f":
    f = " x"
if x6 == "g":
    g = " x"
if x6 == "h":
    h = " x"
if x6 == "k":
    k = " x"
if a==" x"  and b==" x" and c == " x" or c==" x" and f==" x" and k == " x" or g==" x" and h==" x" and k == " x" or a==" x" and d==" x" and g == " x" or a==" x" and e==" x" and k == " x" or g==" x" and e==" x" and c == " x" or d==" x" and e ==" x" and f==" x" or b==" x" and e==" x" and h==" x":
    print("Выграл игрок X!!!")
    print("Выграл игрок X!!!")
    print("Выграл игрок X!!!")
    print(a, b, c)
    print(d, e, f)
    print(g, h, k)
    input('Press ENTER to exit')
    sys.exit()
if a==" 0" and b==" 0" and c == " 0" or c==" 0" and f==" 0" and k == " 0" or g==" 0" and h==" 0" and k == " 0" or a==" 0" and d==" 0" and g == " 0" or a==" 0" and e==" 0" and k == " 0" or g==" 0" and e==" 0" and c == " 0" or d==" 0" and e ==" 0" and f==" 0" or b==" 0" and e==" 0" and h==" 0":
    print("Выграл игрок 0!!!")
    print("Выграл игрок 0!!!")
    print("Выграл игрок 0!!!")
    print(a, b, c)
    print(d, e, f)
    print(g, h, k)
    input('Press ENTER to exit')
    sys.exit()
clear = lambda: os.system('cls')
clear()
print(a, b, c, "       [a]", "[b]", "[c]")
print(d, e, f, "       [d]", "[e]", "[f]")
print(g, h, k, "       [g]", "[h]", "[k]")
x7 = input("Ход игрока 0:  ")
if x1 == x7 or x2 == x7 or x3 == x7 or x4 == x7 or x5 ==x7 or x6 == x7:
    print("Так нельзя")
    x7 = input("Ход игрока 0:  ")
if x7 == "a":
    a = " 0"
if x7 == "b":
    b = " 0"
if x7 == "c":
    c = " 0"
if x7 == "d":
    d = " 0"
if x7 == "e":
    e = " 0"
if x7 == "f":
    f = " 0"
if x7 == "g":
    g = " 0"
if x7 == "h":
    h = " 0"
if x7 == "k":
    k = " 0"
if a==" x"  and b==" x" and c == " x" or c==" x" and f==" x" and k == " x" or g==" x" and h==" x" and k == " x" or a==" x" and d==" x" and g == " x" or a==" x" and e==" x" and k == " x" or g==" x" and e==" x" and c == " x" or d==" x" and e ==" x" and f==" x" or b==" x" and e==" x" and h==" x":
    print("Выграл игрок X!!!")
    print("Выграл игрок X!!!")
    print("Выграл игрок X!!!")
    print(a, b, c)
    print(d, e, f)
    print(g, h, k)
    input('Press ENTER to exit')
    sys.exit()
if a==" 0" and b==" 0" and c == " 0" or c==" 0" and f==" 0" and k == " 0" or g==" 0" and h==" 0" and k == " 0" or a==" 0" and d==" 0" and g == " 0" or a==" 0" and e==" 0" and k == " 0" or g==" 0" and e==" 0" and c == " 0" or d==" 0" and e ==" 0" and f==" 0" or b==" 0" and e==" 0" and h==" 0":
    print("Выграл игрок 0!!!")
    print("Выграл игрок 0!!!")
    print("Выграл игрок 0!!!")
    print(a, b, c)
    print(d, e, f)
    print(g, h, k)
    input('Press ENTER to exit')
    sys.exit()
clear = lambda: os.system('cls')
clear()
print(a, b, c, "       [a]", "[b]", "[c]")
print(d, e, f, "       [d]", "[e]", "[f]")
print(g, h, k, "       [g]", "[h]", "[k]")
x8 = input("Ход игрока x:  ")
if x1 == x8 or x2 == x8 or x3 ==x8 or x5 == x8 or x4 == x8 or x5==x8 or x7 == x8:
    print("Так нельзя")
    x8 = input("Ход игрока x:  ")
if x8 == "a":
    a = " x"
if x8 == "b":
    b = " x"
if x8 == "c":
    c = " x"
if x8 == "d":
    d = " x"
if x8 == "e":
    e = " x"
if x8 == "f":
    f = " x"
if x8 == "g":
    g = " x"
if x8 == "h":
    h = " x"
if x8 == "k":
    k = " x"
if a==" x"  and b==" x" and c == " x" or c==" x" and f==" x" and k == " x" or g==" x" and h==" x" and k == " x" or a==" x" and d==" x" and g == " x" or a==" x" and e==" x" and k == " x" or g==" x" and e==" x" and c == " x" or d==" x" and e ==" x" and f==" x" or b==" x" and e==" x" and h==" x":
    print("Выграл игрок X!!!")
    print("Выграл игрок X!!!")
    print("Выграл игрок X!!!")
    print(a, b, c)
    print(d, e, f)
    print(g, h, k)
    sys.exit()
if a==" 0" and b==" 0" and c == " 0" or c==" 0" and f==" 0" and k == " 0" or g==" 0" and h==" 0" and k == " 0" or a==" 0" and d==" 0" and g == " 0" or a==" 0" and e==" 0" and k == " 0" or g==" 0" and e==" 0" and c == " 0" or d==" 0" and e ==" 0" and f==" 0" or b==" 0" and e==" 0" and h==" 0":
    print("Выграл игрок 0!!!")
    print("Выграл игрок 0!!!")
    print("Выграл игрок 0!!!")
    print(a, b, c)
    print(d, e, f)
    print(g, h, k)
    input('Press ENTER to exit')
    sys.exit()
clear = lambda: os.system('cls')
clear()
print(a, b, c, "       [a]", "[b]", "[c]")
print(d, e, f, "       [d]", "[e]", "[f]")
print(g, h, k, "       [g]", "[h]", "[k]")
x9 = input("Ход игрока 0:  ")
if x1 == x9 or x2 == x9 or x3 == x9 or x4 == x9 or x5 ==x9 or x6 == x9 or x7 ==x9 or x8==x9:
    print("Так нельзя")
    x9 = input("Ход игрока 0:  ")
if x9 == "a":
    a = " 0"
if x9 == "b":
    b = " 0"
if x9 == "c":
    c = " 0"
if x9 == "d":
    d = " 0"
if x9 == "e":
    e = " 0"
if x9 == "f":
    f = " 0"
if x9 == "g":
    g = " 0"
if x9 == "h":
    h = " 0"
if x9 == "k":
    k = " 0"
if a==" x"  and b==" x" and c == " x" or c==" x" and f==" x" and k == " x" or g==" x" and h==" x" and k == " x" or a==" x" and d==" x" and g == " x" or a==" x" and e==" x" and k == " x" or g==" x" and e==" x" and c == " x" or d==" x" and e ==" x" and f==" x" or b==" x" and e==" x" and h==" x":
    print("Выграл игрок X!!!")
    print("Выграл игрок X!!!")
    print("Выграл игрок X!!!")
    print(a, b, c)
    print(d, e, f)
    print(g, h, k)
    sys.exit()
if a==" 0" and b==" 0" and c == " 0" or c==" 0" and f==" 0" and k == " 0" or g==" 0" and h==" 0" and k == " 0" or a==" 0" and d==" 0" and g == " 0" or a==" 0" and e==" 0" and k == " 0" or g==" 0" and e==" 0" and c == " 0" or d==" 0" and e ==" 0" and f==" 0" or b==" 0" and e==" 0" and h==" 0":
    print("Выграл игрок 0!!!")
    print("Выграл игрок 0!!!")
    print("Выграл игрок 0!!!")
    print(a, b, c)
    print(d, e, f)
    print(g, h, k)
    input('Press ENTER to exit')
    sys.exit()
else:
    print("Ничья!!")
    print("Ничья!!")
    print("Ничья!!")
    input('Press ENTER to exit')
    sys.exit()
clear = lambda: os.system('cls')
clear()
print(a, b, c, "       [a]", "[b]", "[c]")
print(d, e, f, "       [d]", "[e]", "[f]")
print(g, h, k, "       [g]", "[h]", "[k]")
