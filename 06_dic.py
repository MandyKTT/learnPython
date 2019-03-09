#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#一个简单的字典
alien_0={'color': 'green', 'points': 5}
print(alien_0)

#添加键-值对
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# 创建一个空字典
alien_0 = {}

# 修改字典中的值
alien_0 = {'color' : 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + '.')

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'midium'}
print("Original x-position: " + str(alien_0['x_position']))

# 向右移动外星人
# 据外星人当前速度决定将其移动多远
if alien_0['speed'] == 'slow' :
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

#删除键
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

#遍历所有的键-值对
user_0={
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
    }
for key, value in user_0.items():
    print("\nKey: " +key)
    print ("Value: " + value)

# 遍历字典中的所有键
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phli': 'python'
    }

for name in favorite_languages.keys():
    print(name.title())

# 遍历所有的值
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phli': 'python'
    }

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

print()

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens=[alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)


# 创建一个用于存储外星人的空列表
aliens = []
#创建30个绿色外星人
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

#显示前五个外星人
for alien in aliens[:5]:
    print(alien)
print("...")

# 在字典中存储列表
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }
# 概述做点的比萨
print("You ordered a " + pizza['crust'] + "-crust pizza "+ "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

users = {
    'aeinstein':{
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
        },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
        },
    }
for username,user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())