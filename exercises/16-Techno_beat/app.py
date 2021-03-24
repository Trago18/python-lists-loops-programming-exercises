
def lyrics_generator(myList):

    string = ''
    count = 0

    for i in myList:
        if (i == 0):
            string += 'Boom '
        elif (i == 1 and count == 2):
            string += 'Drop the base !!!Break the base!!! '
        else:
            string += 'Drop the base '
            count += 1
    
    return string

# Your code go above, nothing to change after this line:
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))