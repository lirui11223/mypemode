from PIL import Image,ImageFilter,ImageDraw,ImageFont

def filter(path,typ):
    img = Image.open(path)
    m = ['进行模糊效果', '进行轮廓效果', '进行细节效果', '边缘加强效果', '让边缘部分更加明显', '进行浮雕效果','进行边界效果', '进行平滑效果', '让图片更平滑', '进行锐化效果']
    while True:
        if typ == 1:
            b = img.filter(ImageFilter.BLUR)
        elif typ == 2:
            b = img.filter(ImageFilter.CONTOUR)
        elif typ == 3:
            b = img.filter(ImageFilter.DETAIL)
        elif typ == 4:
            b = img.filter(ImageFilter.EDGE_ENHANCE)
        elif typ == 5:
            b = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
        elif typ == 6:
            b = img.filter(ImageFilter.EMBOSS)
        elif typ == 7:
            b = img.filter(ImageFilter.FIND_EDGES)
        elif typ == 8:
            b = img.filter(ImageFilter.SMOOTH)
        elif typ == 9:
            b = img.filter(ImageFilter.SMOOTH_MORE)
        elif typ == 10:
            b = img.filter(ImageFilter.SHARPEN)
    return img
