#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
car='bmw'
print(car=='bmw')

requested_topping='mushrooms'
if requested_topping!='anchovies':
    print("Hold the anchovies!")
requested_toppings=['mushrooms','onions','pineapple']
print('mushrooms' in requested_toppings)

banned_users=['andrew','carolina','david']
user='marie'

if user not in banned_users:
    print(user.title()+",you can post a response if you wish.")
age=17
if age>=18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry,you are too young to vote!")
    print("Please register to vote as soon as you turn 18!")
age=12
if age<4:
    print("Your admission cost is $0.")
elif age<18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")
age = 12
if age<4:
    price=0
elif age<18:
    price=5
else:
    price=10

print("Your admission cost is "+ str(price) +'.')

requested_toppings=['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
    if(requested_topping=='green peppers'):
        print("Sorry,we are out of green peppers right now.")
    else:
        print("Adding "+requested_topping+".")

print("\n Finished making your pizza!")"""

#检查列表是否为空
requested_toppings=[]
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Add "+requested_topping+".")
    print("\n Finished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")






