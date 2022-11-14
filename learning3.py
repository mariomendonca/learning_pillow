from PIL import Image
im = Image.open('hello.jpg')

# filename = input('name: ')
print(im.format, im.size, im.mode)

box = (100, 100, 200, 200)
region = im.crop(box)
region.show()
region = region.transpose(Image.Transpose.ROTATE_180)
im.paste(region, box)
im.show()

# testing = region.transpose(Image.Transpose.ROTATE_270)
# testing.show()




# im.save(f'{filename}.jpg')

# (left, upper, right, lower