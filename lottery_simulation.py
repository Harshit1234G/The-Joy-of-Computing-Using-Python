import matplotlib.pyplot as plt
from random import randint

x = []
y = []
balance = 0

for i in range(365):
    x.append(i)
    bet = randint(1, 10)
    lucky_draw = randint(1, 10)

    if bet == lucky_draw:
        balance += 800

    else:
        balance -= 100
    y.append(balance)

plt.plot(x,y)
plt.show()
print(y[-1])