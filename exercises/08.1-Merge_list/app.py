chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']


def merge_list(list1, list2):
    
    merge_list = []
    for i in chunk_one:
        merge_list.append(i)
    for i in chunk_two:
        merge_list.append(i)
    return merge_list
    
print(merge_list(chunk_one, chunk_two))
