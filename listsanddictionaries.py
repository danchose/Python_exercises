"""animals = []
animals.append("tiger")
animals.append("lion")
animals.remove("tiger")
animals.extend(["zebra", "elephant", "giraffe", "hippos"])
print(animals)
print(animals.index("zebra"))
other_animals = animals[:]
other_animals.append("hyena")
print(animals)
print(other_animals)
"""
"""two_by_two = [[1,2], [6, 3]]
print(two_by_two[0][0])

groceries_str = ("eggs, ham, potato, salad")
groceries_list = groceries_str.split(", ")
print(groceries_list)
print(groceries_list[0])
"""
def list_sort(list):
    for i in list:
        if i >= 1 and i <= 20:
            print(i)

list = [2, 4, 8, 16, 32, 64]
list_sort(list)

"""desserts = ["ice cream", "cookies"]
desserts.sort()
food = desserts[:]
food.extend(["broccoli", "turnips"])
food.remove("cookies")
print("Food list is:", food[:2])
print("Desserts list is: ",desserts)

breakfast_s = ("cookies, cookies, cookies")
breakfast = breakfast_s.split(", ")
print(breakfast)"""