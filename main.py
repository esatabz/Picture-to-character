# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from PIL import Image
ascii_char = list("QWQERTYUIOPASDFGHJKLZXCVBNMkhjouyfukajsf")
#由于字符因素，宽高比尽量2.5：1
WIDTH = 150
HEIGHT = 50
def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ''
    length = len(ascii_char)
    #灰度值公式：Gray=0.2126×R+0.7152×G+0.0722×B
    gray = int(0.2126*r+0.7152*g+0.0722*b)
    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    img = 'G:\图片\新建文件夹\QQ_Images\-ah.jpg'
    im = Image.open(img)
    im = im.resize((WIDTH,HEIGHT),Image.NEAREST)
    txt = ""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'
    print(txt)
    #print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
