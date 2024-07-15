calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    
    count_calls() 
    return len(string), string.upper(), string.lower()

def is_contains(string, list_to_search):
    
    count_calls() 
    return string.upper() in [item.upper() for item in list_to_search]


print(string_info("Hello, World!"))
print(is_contains("Urban", ["URBAN", "CITY", "TOWN"]))
print(string_info("Python"))
print(is_contains("python", ["Ruby", "Java", "c++", "Python"]))

print(f"Количество вызовов функций: {calls}")