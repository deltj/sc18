from PIL import Image
from qrtools import QR
import itertools

imgs = []

for i in range(0, 27):
    #print str(i) + ".png"
    imgs.append(Image.open(str(i) + ".png"))


qrimg = Image.new("RGB", (230, 297))
# left margin
qrimg.paste(imgs[13], (0, 0))

# first square order: 5 6 25 16 2 15 26
qrimg.paste(imgs[5],  (10, 0))   # 1
#qrimg.paste(imgs[6],  (20, 0))
#qrimg.paste(imgs[25], (30, 0))
qrimg.paste(imgs[16], (40, 0))
qrimg.paste(imgs[2],  (50, 0))
qrimg.paste(imgs[15], (60, 0))
qrimg.paste(imgs[26], (70, 0))

# pretty sure this goes here
qrimg.paste(imgs[3],  (80, 0))

# center part, not so sure
#perms = list(itertools.permutations([1, 2, 3]))
#qrimg.paste(imgs[23], (90, 0))   # 9
#qrimg.paste(imgs[19], (100, 0))
#qrimg.paste(imgs[21], (110, 0))  # 11
#qrimg.paste(imgs[10], (120, 0))
qrimg.paste(imgs[20], (130, 0))

# pretty sure this goes here
qrimg.paste(imgs[7],  (140, 0))

# last square order: 8 1 24 4 22 18 14
qrimg.paste(imgs[8],  (150, 0))   # 15
qrimg.paste(imgs[1],  (160, 0))
#qrimg.paste(imgs[24], (170, 0))   # 17
#qrimg.paste(imgs[4],  (180, 0))
#qrimg.paste(imgs[22], (190, 0))
qrimg.paste(imgs[18], (200, 0))
qrimg.paste(imgs[14], (210, 0))

# right margin
qrimg.paste(imgs[17], (220, 0))

# columns 2-3 could be swapped
for a in [(6, 25), (25, 6)]:
    qrimg.paste(imgs[a[0]],  (20, 0))
    qrimg.paste(imgs[a[1]], (30, 0))

    # columns 9-11 could be swapped
    for b in [(23, 21), (21, 23)]:
        qrimg.paste(imgs[b[0]], (90, 0))
        qrimg.paste(imgs[b[1]], (110, 0))

        # columns 10-12 could be swapped
        for c in [(19, 10), (10, 19)]:
            qrimg.paste(imgs[c[0]], (100, 0))
            qrimg.paste(imgs[c[1]], (120, 0))

            # columns 17-19 could be any permutation
            for d in itertools.permutations([24, 4, 22]):
                qrimg.paste(imgs[d[0]], (170, 0))
                qrimg.paste(imgs[d[1]], (180, 0))
                qrimg.paste(imgs[d[2]], (190, 0))

                # try it
                qrimg.save("foo.png", "PNG")

                #qr = QR(qrimg)
                qr = QR(filename = "foo.png")
                qr.decode()
                print qr.data
