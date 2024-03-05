from PIL import Image

img = Image.open("crime_scene.jpg")

transposed_img = img.transpose(Image.FLIP_LEFT_RIGHT)

transposed_img.save('fliped_crime_scene.jpg')

print("Done flipping")

import cv2

img = cv2.imread('crime_scene.jpg')
clahe = cv2.createCLAHE()

gray_scale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite('enhanced_img.jpg', clahe.apply(gray_scale))