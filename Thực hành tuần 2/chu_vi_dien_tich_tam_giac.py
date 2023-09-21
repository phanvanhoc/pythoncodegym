import math
a = float(input("nhập số cạnh thứ 1:"))
b = float(input("nhập số cạnh thứ 2:"))
c = float(input("nhập số cạnh thứ 3:"))
s = (a+b+c)/2
d = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("chu vi tam giác là :", s)
print("diện tích tam giác là :", d)
