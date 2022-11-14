from PIL import Image
im1 = Image.open('download.jpeg')
im2 = Image.open('jame.jpeg')

print(im1.size)
# point = (20, 200)
point = (30, 30)
# im1.show()
im2 = im2.resize(point)
# im1 = im1.resize(point)


im1.paste(im2, point)
im1.show()
# im1.paste(im1, im2)
# im1.show()
