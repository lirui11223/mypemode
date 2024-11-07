import easygui
from PIL import Image,ImageFilter,ImageDraw,ImageFont

def filter(path,msg,title):
    img = Image.open(path)
    m = ['进行模糊效果', '进行轮廓效果', '进行细节效果', '边缘加强效果', '让边缘部分更加明显', '进行浮雕效果','进行边界效果', '进行平滑效果', '让图片更平滑', '进行锐化效果']
    use = easygui.choicebox(msg,title,m)
    while True:
        if use == '进行模糊效果':
            b = img.filter(ImageFilter.BLUR)
        elif use == '进行轮廓效果':
            b = img.filter(ImageFilter.CONTOUR)
        elif use == '进行细节效果':
            b = img.filter(ImageFilter.DETAIL)
        elif use == '边缘加强效果':
            b = img.filter(ImageFilter.EDGE_ENHANCE)
        elif use == '让边缘部分更加明显':
            b = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
        elif use == '进行浮雕效果':
            b = img.filter(ImageFilter.EMBOSS)
        elif use == '进行边界效果':
            b = img.filter(ImageFilter.FIND_EDGES)
        elif use == '进行平滑效果':
            b = img.filter(ImageFilter.SMOOTH)
        elif use == '让图片更平滑':
            b = img.filter(ImageFilter.SMOOTH_MORE)
        elif use == '进行锐化效果':
            b = img.filter(ImageFilter.SHARPEN)
        elif use == None:
            c = easygui.msgbox(msg,title,'是')
            if use != None:
                img.show()
                break