myNumbers = [23,234,345,4356234,243,43,56,2]

def increment_by_one(x):
    return x*3

new_list = list(map(increment_by_one, myNumbers))
#new_list = list(map(lambda x: x * 3, myNumbers))

print(new_list)