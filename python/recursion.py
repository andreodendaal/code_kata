import random


def find_something(find_object):

    if random.choice([False, True]):
        print("Found a {}!".format(find_object))
        return True
    else:
        print("Found nothing!")
        return False


def look_in_boxes(find_object):

    found = find_something(find_object)
    while not found:
        print("look in next box")
        return look_in_boxes(find_object)

    return found


print('Looking in first Box')
print(look_in_boxes('key'))





