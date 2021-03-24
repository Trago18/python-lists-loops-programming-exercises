incomingAJAXData = [
	{ "name": 'Mario', "lastName": 'Montes' },
	{ "name": 'Joe', "lastName": 'Biden' },
	{ "name": 'Bill', "lastName": 'Clon' },
	{ "name": 'Hilary', "lastName": 'Mccafee' },
	{ "name": 'Bobby', "lastName": 'Mc birth' }
]

def my_var(x):
    return (f'{x["name"]} {x["lastName"]}')
    
transformedData = list(map(my_var, incomingAJAXData))

print(transformedData)