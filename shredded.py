from PIL import Image

imgs = []

for i in range(0, 27):
    #print str(i) + ".png"
    imgs.append(Image.open(str(i) + ".png"))


qrimg = Image.new("RGB", (210, 297))
# first square order: 5 6 25 16 2 15 26
qrimg.paste(imgs[5], (0, 0))
qrimg.paste(imgs[6], (10, 0))
qrimg.paste(imgs[25], (20, 0))
qrimg.paste(imgs[16], (30, 0))
qrimg.paste(imgs[2], (40, 0))
qrimg.paste(imgs[15], (50, 0))
qrimg.paste(imgs[26], (60, 0))

qrimg.save("foo.png", "PNG")
