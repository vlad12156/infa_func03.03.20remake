nome  = int(input("Увести номер послуги: "))
if nome == 1:
  print("Поштова і кур'єрська діяльність")
elif nome == 2:
  print("Телеграфний зв'язок")
elif nome == 3:
  print("Фіксований телефонний зв'язок")
elif nome == 4:
  print("мобільний зв'язок")
elif nome == 5:
  print("супутниковий зв'язок")
elif nome == 6:
  print("трансляція теле-і радіо-програм")
elif nome == 7:
  print("проводове мовлення")
elif nome == 8:
  print("нтернет-послуги")
elif nome == 9:
  print("Інші види послуг")

a = int(input("Доход послуги: "))
b = int(input("Доход послуги: "))
c = int(input("Доход послуги: "))
d = int(input("Доход послуги: "))
e = int(input("Доход послуги: "))
f = int(input("Доход послуги: "))
g = int(input("Доход послуги: "))
k = int(input("Доход послуги: "))
l = int(input("Доход послуги: "))

a1 = a
a2 = b
a3 = c
a4 = d
a5 = e
a6 = f
a7 = g
a8 = k
a9 = l

def func(a1,a2,a3,a4,a5,a6,a7,a8,a9):
    return (a1+a2+a3+a4+a5+a6+a7+a8+a9)
print(func(1,2,3,4,5,6,7,8,9))

