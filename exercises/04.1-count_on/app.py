
my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]

hello = []

for i in my_list:
    if (type(i) == type({}) or type(i) == type([])):
        hello.append(i)

print(hello)
