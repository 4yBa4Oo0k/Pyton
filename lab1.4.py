#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = [ 'mother, brother1, brother2, grandfather, grandmother']


# список списков приблизителного роста членов вашей семьи
my_family_height = [ ['mother', 170], ['brother1', 160], ['brother2', 76], ['grandfather', 177], ['grandmother', 175]]
    # ['имя', рост],


# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
print ('grandfathers height -', my_family_height [4][1])
print ('overall family growth-', my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1] + my_family_height[3][1] + my_family_height[4][1])
 