"""
На Новом проспекте построили подряд 10 зданий.
Каждое здание может быть либо жилым домом, либо магазином, либо офисным зданием.

Но оказалось, что жителям некоторых домов на Новом проспекте слишком далеко
приходится идти до ближайшего магазина. Для разработки плана развития общественного
транспорта на Новом проспекте мэр города попросил вас выяснить, какое же наибольшее
 расстояние приходится преодолевать жителям Нового проспекта, чтобы дойти от своего дома до ближайшего магазина.

Формат ввода
Программа получает на вход десять чисел,
разделенных пробелами. Каждое число задает тип здания на Новом проспекте:
число 1 обозначает жилой дом, число 2 обозначает магазин, число 0 обозначает офисное здание.
Гарантируется, что на Новом проспекте есть хотя бы один жилой дом и хотя бы один магазин.
"""

street = list(map(int, input().split()))

shop_indexes = []
houses_indexes = []

for i in range(len(street)):
    if street[i] == 2:
        shop_indexes.append(i)
    elif street[i] == 1:
        houses_indexes.append(i)

diffs = []
for house in houses_indexes:
    every_diff = []
    for shop in shop_indexes:
        every_diff.append(abs(shop - house))
    diffs.append(min(every_diff))

print(max(diffs))