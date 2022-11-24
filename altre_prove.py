import matplotlib.pyplot as plt
import random


for i in range(3):
    plt.plot([random.randint(1,5),random.randint(1,5),random.randint(1,5)])

plt.ylabel('soldi')
plt.show()


