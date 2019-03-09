#!/usr/bin/env python 
# -*- coding:utf-8 -*-

"""
# input()
name=input("Please enter your name:")
print("Hello," + name + "!")

# int()
height = input("How tall are you?")
height = int(height)
if height >= 36:
    print("yes")
else:
    print("no")

# 取模运算 %
print(4 % 3)"""

# 让用户选择何时退出
prompt = "\nTell me something, and I will repeat it right back to you!"
prompt += "\nEnter 'quit' to end this program."

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)


