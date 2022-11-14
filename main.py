from PIL import Image

hair = Image.open('jame_hair.png')
img = Image.open('img.png')

# w, h = img.size
print(hair.size)
hair = hair.resize((135, 135))
hair.show()
point = (35, -2)

img.paste(hair, point, hair)
# img.paste(hair, point)
img.show()