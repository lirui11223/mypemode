from PIL import Image,ImageDraw,ImageFont
import random,easygui

def yzcode(width,height,pngname):
    w=width
    h=height
    img=Image.new('RGB',(w,h),'white')#图片对象
    t=ImageDraw.Draw(img)#可绘制图片对象
    for x in range(w):
        for y in range(h):
            r=random.randint(100,255)
            g=random.randint(100,255)
            b=random.randint(100,255)
            t.point((x,y),(r,g,b))
    f=ImageFont.truetype('simhei.ttf',36)#字体对象
    col = ['red','orange','yellow','green','blue','purple','pink','black','white']
    leter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    p1 = random.choice(['n','s'])
    if p1 == 'n':
        c1=str(random.randint(0,9))
        c1c = random.choice(col)
    else:
        c1 = random.choice(leter)
        c1c = random.choice(col)
    p2 = random.choice(['n','s'])
    if p2 == 'n':
        c2=str(random.randint(0,9))
        c2c = random.choice(col)
    else:
        c2 = random.choice(leter)
        c2c = random.choice(col)
    p3 = random.choice(['n','s'])
    if p3 == 'n':
        c3=str(random.randint(0,9))
        c3c = random.choice(col)
    else:
        c3 = random.choice(leter)
        c3c = random.choice(col)
    p4 = random.choice(['n','s'])
    if p4 == 'n':
        c4=str(random.randint(0,9))
        c4c = random.choice(col)
    else:
        c4 = random.choice(leter)
        c4c = random.choice(col)
    p5 = random.choice(['n','s'])
    if p5 == 'n':
        c5=str(random.randint(0,9))
        c5c = random.choice(col)
    else:
        c5 = random.choice(leter)
        c5c = random.choice(col)
    num = c1+c2+c3+c4+c5
    t.text((5,8),text=num,fill='red',font=f)
    t.line((0,20,w,h-20),'green',3)
    t.line((20,h,w-20,0),(0,255,0),3)
    img.save(pngname)