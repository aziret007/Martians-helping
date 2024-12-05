import random

a = range(7)
location = random.sample(a, k=3)
weight = 713

while True:
    print(location)
    b = list(map(int, input('Enter the location 3 numbers with space: ').split()))
    enterWeight = sum(list(map(int, input('Enter the weight 3 numbers with space: ').split())))

    if location == b and weight == enterWeight:
        print('U did it')
        break
    else:
        print('Wrong')
        location = random.sample(a, k=3)