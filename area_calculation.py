from PIL import Image
# import numpy as np
from random import randrange

img = Image.open('rajasthan.jpg')
# print(img)
data = img.load()
# img.show()
# print(data)
# print(np.array(img))
# rgb_img = img.convert('RGB')
# r, g, b = img.getpixel(())
# print(r, g, b)

raj, ind = 0, 0

for _ in range(1000000):
    x = randrange(0, img.width)
    y = randrange(0, img.height)

    # print(x, y)
    # print(data[x, y])

    if data[x, y][0] == 2:
        raj += 1

    elif data[x, y][0] == 179:
        ind += 1

print(f"Area of Rajastha: {raj / ind * 32_87_263 }")