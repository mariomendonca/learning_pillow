from PIL import Image
im = Image.open('hello.jpg')

# def roll(im, delta):
#   xsize, ysize = im.size
#   delta = delta % xsize
#   if delta == 0:
#       return im

#   part1 = im.crop((0, 0, delta, ysize))
#   part2 = im.crop((delta, 0, xsize, ysize))
#   im.paste(part1, (xsize - delta, 0, xsize, ysize))
#   im.paste(part2, (0, 0, xsize - delta, ysize))

#   return im

# roll(im, 200).show()

def merge(im1, im2):
  w = im1.size[0] + im2.size[0]
  h = max(im1.size[1] , im2.size[1])
  im = Image.new("RGBA", (w,h))

  im.paste(im1)
  im.paste(im2, (im1.size[0], 0))

  return im

# merge(im, im).show()

# im.show()
# r,g,b = im.split()
# im = Image.merge("RGB", (b,g,r))
# im.show()

# out = im.resize((128,128))
# out.show()
# out = im.rotate(45)
# out.show()
# out = im.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
# out.show()
# out = im.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
# out.show()

im = im.convert('L')
im.show()
# out = im.transpose(Image.Transpose.ROTATE_90)
# out.show()
# out = im.transpose(Image.Transpose.ROTATE_180)
# out.show()
# out = im.transpose(Image.Transpose.ROTATE_270)
# out.show()