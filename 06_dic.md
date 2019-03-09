## 使用字典
在Python中，字典是一次了 键-值 对。每个键都与一个值相关联，你可以使用键来访问与之相关联的值。与键相关联的值可以是数字、字符串、列表乃至字典。事实上，可将任何Python对象用作字典中的值。
在Python中，字典用放在花括号{ }中的一系列键-值对表示，例如：
```
alien_0={'color': 'green', 'points': 5}
```
键-值对是两个相关联的值。指定键是，Python将返回与之相关联的值。键和值之间用冒号分隔，而键-值对之间用逗号分隔。
### 如何访问字典中的值
要获取与键相关联的值，可一次指定字典名和放在方括号内的键，如下所示：

```python
alien_0={'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])
```
输出结果：

	green
	5
### 添加键-值对
字典是一种动态结构，可随时在其中添加键-值对。要添加键-值对，可一次指定字典名、用方括号括起得键和相关联的值。

例：下面在字典alien_0中添加两项信息：外星人的x坐标和y坐标，让我们能够在屏幕的特定位置显示该外星人。

```python
alien_0={'color': 'green', 'points': 5}
print(alien_0)

#添加键-值对
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
```
这个字典的最终版本包含四个键-值对：
	
	{'color': 'green', 'points': 5}
	{'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}

### 修改字典中的值
要修改字典中的值，可一次指定字典名、用方括号括起得键以及与该键相关联的新值。
例，假设随着游戏的进行，需要将一个外星人从绿色改为黄色：

```python
alien_0 = {'color' : 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + '.')
```
输出表明，这个外形恩确实从绿色变成了黄色：

	The alien is green.
	The alien is now yellow.
### 删除键-对
对于字典中不需要的信息，可使用del语句将相应的键-值对彻底删除。使用del语句时，必须制定字典名和要删除的键。
例，从字典alien_0中删除键‘points’及其值：

```python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)
```
删除键‘points’后，输出结果：

	{'color': 'green', 'points': 5}
	{'color': 'green'}
删除的键-值对永远消失了。

## 遍历字典
### 遍历所有的键-值对
例，遍历下面的字典存储的每一用户：

```python
user_0={
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
    }
for key, value in user_0.items():
    print("\nKey: " +key)
    print ("Value: " + value)
```
for语句的第二部分包含字典名和方法items（），它返回一个键-值对列表。接下来for循环一次将每个键-值对存储到指定的两个变量中。

	Key: username
	Value: efermi

	Key: first
	Value: enrico

	Key: last
	Value: fermi
### 遍历字典中的所有键
在不需要使用字典中的值时，方法keys（）很有用。

```python
# 遍历字典中的所有键
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phli': 'python'
}

for name in favorite_languages.keys():
    print(name.title())
```
输出结果：

	Jen
	Sarah
	Edward
	Phli
### 遍历所有的值
如果你感兴趣的是字典中的值，可使用方法values（），它返回一个值列表，而不包含任何键。
例，我们想要获取的列表只包含被调查者选择的各种语言，而被调查者是匿名的：

```python
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
```
输出结果：

	The following languages have been mentioned:
	Python
	C
	Ruby
	Python
## 嵌套
有时候，需要将一系列字典存储在列表中，或将列表作为值存储在字典中，这成为嵌套。
可以在列表中嵌套字典、在字典中嵌套列表甚至在字典中嵌套字典。
### 字典列表
例，下面的代码创建一个包含三个外星人的列表：

```python
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens=[alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
```
输出结果：

	{'color': 'green', 'points': 5}
	{'color': 'yellow', 'points': 10}
	{'color': 'red', 'points': 15}

### 在字典中存储列表
有时候需要将列表存储在字典中，而不是将字典存储在列表中。

```python
# 在字典中存储列表
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }
# 概述做点的比萨
print("You ordered a " + pizza['crust'] + "-crust pizza "+ "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)
```
输出结果：

	You ordered a thick-crust pizza with the following toppings:
		mushrooms
		extra cheese
### 在字典中存储字典
可在字典中嵌套字典，但这样做时，代码可能很快复杂起来。
例，如果有多个网站用户，每个都有独特的用户名，可在字典中将用户名作为键，然后将美味用户的信息存储在一个字典中，并将该字典作为与用户相关联的值。

```python
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
```
上例代码首先定义了一个名为users的字典，其中包含两个键：用户名‘aeinstein’和‘mcurie’；与每个键相关联的值都是一个字典，其中包含用户的名、姓和居住地。

	Username: aeinstein
		Full name: Albert Einstein
		Location: Princeton

	Username: mcurie
		Full name: Marie Curie
		Location: Paris
