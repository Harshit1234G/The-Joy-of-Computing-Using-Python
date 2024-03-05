from PIL import Image

im = Image.open('img.jpg').convert('L')
data_im = im.load()

new_im = Image.new(im.mode, im.size)
data_new = new_im.load()

for i in range(im.width):
    for j in range(im.height):
        if data_im[i, j] >= 0 and data_im[i, j] <= 31:
            data_new[i, j] = 0

        elif data_im[i, j] >= 32 and data_im[i, j] <= 63:
            data_new[i, j] = 1

        elif data_im[i, j] >= 64 and data_im[i, j] <= 95:
            data_new[i, j] = 2

        elif data_im[i, j] >= 96 and data_im[i, j] <= 127:
            data_new[i, j] = 3

        elif data_im[i, j] >= 128 and data_im[i, j] <= 159:
            data_new[i, j] = 4

        elif data_im[i, j] >= 160 and data_im[i, j] <= 191:
            data_new[i, j] = 5

        elif data_im[i, j] >= 192 and data_im[i, j] <= 223:
            data_new[i, j] = 6

        elif data_im[i, j] >= 224 and data_im[i, j] <= 255:
            data_new[i, j] = 7

new_im.save("Compressed_img.jpg")