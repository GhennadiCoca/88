#list
from QA_88M.Lesson_01.type_strings import coordinate

fruits = ["apple", "banana", "cherry"]
nubers = [1,2,3,4,5,6,7,8,9,10]
mix = ["text",56,34.7, True,True]
empty = []

print(type(empty))
print("length of nubers:",len(nubers))
print("leght of fruits:",len(fruits))

print(fruits[1])
print(fruits[::-1])
print(fruits[-1])

fruits[1] = 'orange'
print(fruits)

fruits.append('lemon')
print(fruits)

fruits.insert(1,"kiwi")
print(fruits)

fruits.remove("kiwi")
print(fruits)

last = fruits.pop()
print(last)
print(fruits)

numbers2 = [99, 1, 2, 34, 4, 5, 78, 7, 0, 9, 10]
print(sorted(numbers2))
print(sorted(numbers2, reverse=True))
print(min(numbers2), max(numbers2), sum(numbers2))
print("Is 34 in numbers2 -->", 34 in numbers2)

numbers2.sort()
print(numbers2)

for fruits in fruits:
    print("I like", fruits)

#tuple
coordinates1 = (10, 20)
single = (34)
print(type(coordinates1))
print(type(single))
tuple1 = 1,2,3
print(type(tuple1))

print(coordinates1[0])
print(coordinates1[-1])

x,y = coordinates1
print(f"x = {x}, y = {y}")

#dict
person = {
    "name": "Sveta",
    "age": 22,
    "city": "Berlin"
}

print(person)
print("Length in my dict:",len(person))
print(person["name"])
print(person["city"])
#print(person["email"])
print(person.get("email"))
print(person.get("email", "not found"))

person["email"] = "knjnk@jkj.cim"
print(person)
person["age"] = 32
print(person)

del person["city"]
print(person)

print("name" in person)
print("phone" in person)

dict_any = {
    1: "paz",
    "two": 2,
    (0,1): "sdff"
}
dict_any[(True,False)] = True
print(dict_any)
dict_any[(False,True)] = "new znacenie"
print(dict_any)

print((True, False)) == (1,0)

prices = {
    "apple": 1,
    "banana": 2,
    "cherry": 3,

}
for product in prices:
    print("product", product)

for product, price in prices.items():
    print(f"product: {product}, price: {price}$")

print(list(prices.keys()))
print(list(prices.values()))
print(sum(prices.values()))

# set
colors = {"red", "green", "blue"}
print(colors)
colors.discard("red")
print("green" in colors)
numbers_set = {1, 2, 10, 4, 5, 6, 6, 8, 1, 10}
print(numbers_set)

empty_dict = {}
print(type(empty_dict))
empty_set = set()
print(type(empty_set))

colors.add("yellow")
print(colors)

names = ["Ivan", "Jose", "Nina", "Ivan"]
print(names)

unique_names = set(names)
print(unique_names)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1 | set2)
print(set1 & set2)
print(set1 - set2)
print(set2 - set1)
print(set1 ^ set2)