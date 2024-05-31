# a = float(input("Введите дробное число"))
# a = int(a * 10)
# print(a % 10)
# x = "я"
# b = "фиалки"
# print(b.index("а"))
# print(x in b)
# letters = 'abcdefghijklmnopqrstuvwxyz'
# print(letters.index("p"))
# print(letters.index("y"))
# print(letters.index("t"))
# print(letters.index("h"))
# print(letters.index("o"))
# print(letters.index("n"))
# b = ("фиалки")
# a = b.upper()
# print(a)
# print(b.lower())
# print(len(b))
# line_1 = "Python"
# line_2 = "Java"
# line_3 = "Go"
# a = len(line_2) + len(line_1) + len(liяne_3)
# print(a/3)
# line_2 = "Java"
# print(line_2.count("a", 1, 3))
# y = "i like java"
# print(y.replace("java", "python"))
# story = "Ехал грека через реку, видит грека - в реке рак. Сунул грека руку в реку, рак за руку греку - цап!"
# old = input("Введите слово, которое нужно заменить: ")
# new = input("Введите слово-заменитель: ")
# print(story.replace(old, new))
# x = 'АБРАКАДАБРА'
# y =  '12-08-2034'
# z = x[2:8:2]
# d = y[1:6:2]
# print(z)
# print(d)
# print(2**8 == 256)
#
# is_raining = True
# if is_raining:
#     print(1)

# ril = float(input("Число:" ))
#
# if ril%2 == 0:
#     print("1")
# else:
#     print("0")
# sss = input()
# predloz = sss.lower()
# print(predloz.count(" ") + 1)
# if predloz.count("хороший") >= 1:
#     print("Слово хороший присутствует")
# order_cost = 250 # стоимость заказа
# discount_cost = 1 # множитель скидки. Если 1, то платят полную стоимость, если 0, то не платят ничего.
#
# age = int(input("Введите свой возраст: "))
#
# if age < 18:
#     discount_cost = 0.95
# elif age < 30:
#     discount_cost = 0.85
# elif age < 60:
#     discount_cost = 0.75
# elif age < 100:
#     discount_cost = 0.5
#
# print("Стоимость заказа со скидкой:", order_cost * discount_cost)
# a = int(input())
# b = int(input())
# c = int(input())
# if a > b and a > c:
#     print(a)
# elif b > a and b > c:
#     print(b)
# elif c > a and c > b:
#     print(c)
# else:
#     print("Числа равны")
# import random
# x = random.randint(0, 3)
# y = int(input("Введите число от 1 до 3, где 1-камень, 2-ножницы, 3-бумага"))
# print(x)
# if x == y:
#     print("Ничья")
# elif y == 3:
#     if x == 2:
#         print("Вы проиграли")
#     else:
#         print("Вы выиграли")
# elif y == 2:
#     if x == 1:
#         print("Вы проиграли")
#     else:
#         print("Вы выиграли")
# elif y == 1:
#     if x == 3:
#         print("Вы проиграли")
#     else:
#         print("Вы выиграли")
# else:
#     print("Такого числа нет")

# day = 1
# while day <= 30:
#     print(f"Сегодня {day} сентября")
#     day += 1

# import random
#
# attempts = 0
# x = random.randint(0, 5)
# y = int(input("Введите число от 1 до 5"))
# while x != y and attempts < 3:
#     y = int(input("Введите число от 1 до 5"))
#     print("Неудача")
#     attempts += 1
#
# if y == x:
#     print("Удача!")
# else:
#     print("Ты проиграл")

# a = 0
# for i in range(101):
#     if i % 2 == 0:
#         a += i
#
#
# print(a)

# number = int(input("number:"))
# a = 0
#
# for i in range(3, number, 3):
#     a += i
#
# print(a)
# number = int(input("number:"))
# a = 0
#
# for i in range(1, number + 1 ):
#     if i % 2 == 0:
#         a = a - i ** i
#     else:
#         a = a + i ** i
#
# print(a)
# import turtle as t
# import  random
# t.shape("turtle")
#
# t.pencolor("blue")
# for i in range(10):
#     x = random.randint(30, 100)
#     for j in range(4):
#         t.fd(x)
#         t.rt(90)
#     t.goto(random.randint(-200, 200), random.randint(-200, 200))
# t.dot(20)
# t.circle(40)
# t.speed(0)
# size = 5
# for i in range(6):
#     t.fd(50)
#     t.lt(60)
# t.mainloop()
