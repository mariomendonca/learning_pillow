from PIL import Image
im = Image.open('image.jpg')

filename = input('name: ')
print(im.format, im.size, im.mode)
im.show()
im.save(f'{filename}.jpg')