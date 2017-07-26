def small_generator(input):
    for value in input:
        yield str(value)

source = [1,3,7,9,11,17]

for prm in small_generator(source):
    print(prm)
