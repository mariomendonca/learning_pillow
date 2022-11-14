from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def watermark_Image(img_path,output_path, text, pos):
    img = Image.open(img_path)
    drawing = ImageDraw.Draw(img)
    black = (10, 5, 12)
    drawing.text(pos, text, fill=black)
    img.show()
    img.save(output_path)
img = 'image.jpg'

watermark_Image(img, 'hello.jpg','aaaaalolo', pos=(30, 30))
