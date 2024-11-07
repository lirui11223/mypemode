import easygui
from PIL import Image,ImageFilter,ImageDraw,ImageFont

def keep(path):
    img = Image.open(path)
    color_choice = easygui.choicebox('请选择要保留的通道','my_picture',['保留红色通道','保留绿色通道','保留蓝色通道'])
    if color_choice == '保留红色通道':
        color = 'r'
    elif color_choice == '保留绿色通道':
        color = 'g'
    elif color_choice == '保留蓝色通道':
        color = 'b'
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