#Словари

my_dict = {"Marat": 2001, "Kostya": 1997, "Dima": 1996}
print(my_dict)
print(my_dict["Marat"])
print(my_dict.get("Katya", "Ключ не найден"))
my_dict["Karina"] = 2000
my_dict["Olga"] = 1999
print(my_dict)
deleted_value = my_dict.pop("Olga")
print(deleted_value)
print(my_dict)

#Множества

my_set = {2,3,2,5,4,5,4,1,2,1, "True", "World", "World"}
print(my_set)
my_set.add("Hello")
my_set.add(6)
my_set.remove("World")
print(my_set)
           
           










