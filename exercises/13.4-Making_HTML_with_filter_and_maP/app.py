all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

# def filter_colors(color):
#     if color["sexy"] == True:
#         return color["label"]

# colors = list(filter(filter_colors, all_colors))

# def generate_li(color):
#     return f'<li>{color["label"]}</li>'

# li = ''.join(map(generate_li, colors))

# print(li)

filter_colors = list(filter(lambda color: color["sexy"] == True, all_colors))

generate_li = ''.join(map(lambda color: f'<li>{color["label"]}</li>' , filter_colors))

print(generate_li)