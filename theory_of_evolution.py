from random import randint

def evolve(data):
    index = randint(0, len(data) - 1)
    probability = randint(1, 100)

    if probability == 1:
        if data[index] == '0':
            data[index] = '1'
        else: 
            data[index] = '0'

with open('dna_data.txt') as f:
    temp = f.read()
    data = list(temp)

for _ in range(1000000):
    evolve(data)

data = ''.join(data)

print(data)
print(data == temp)