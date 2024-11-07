import easygui
from PIL import Image,ImageFilter,ImageDraw,ImageFont

def welcome(msg,title):
        easygui.msgbox(msg, title, '进入程序')