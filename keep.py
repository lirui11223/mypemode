from PIL import Image,ImageFilter,ImageDraw,ImageFont

def keep(path,color):
    img = Image.open(path)
    w = img.width
    h = img.height
    for x in range(w):
        for y in range(h):
            l = img.getpixel((x, y))
            r = l[0]
            g = l[1]
            b = l[2]
            if color == 'r':
                img.putpixel((x, y), (r, 0, 0))
            elif color == 'g':
                img.putpixel((x, y), (0, g, 0))
            elif color == 'b':
                img.putpixel((x, y), (0, 0, b))
    img.show()
