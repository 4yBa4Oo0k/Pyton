#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
# TODO здесь ваш код
zoo.insert(1, "bear")
print (zoo)
# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
i = 0
for chicen in birds:
    zoo.append (chicen)
    i+=1
print (zoo)


#  и выведите список на консоль
# TODO здесь ваш код

print (zoo)

# уберите слона
#  и выведите список на консоль
# TODO здесь ваш код
removed_item = zoo.pop(3)
print (zoo)
# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
# TODO здесь ваш код
print ('lion - 1')
print ('lark - 7')