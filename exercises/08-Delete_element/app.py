people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

def deletePerson(person_name):
    newList = []
    for i in people:
        if (i == person_name):
            continue
        else:
            newList.append(i)
    return newList
    
print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))