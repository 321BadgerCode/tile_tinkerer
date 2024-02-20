from PIL import Image

mask = [
    [(000,000,255),(255,000,000)],
    [(255,000,000),(000,000,255)],
]
iterations = 6
pic = mask


def tupleScale(t, m):
    return tuple(map(lambda e: e * m, t))


def tupleAdd(a, b):
    return tuple((a[i] + b[i] for i in range(len(a))))


for i in range(iterations):
    # square the pic
    npic = [[0 for _ in range(len(pic[0]) * len(mask[0]))] for _ in range(len(pic) * len(mask))]
    for y in range(len(pic)):
        for x in range(len(pic[0])):
            for y1 in range(len(mask)):
                for x1 in range(len(mask[0])):
                    npic[y + y1 * len(pic)][x + x1 * len(pic[0])] = tupleAdd(tupleScale(pic[y][x], 0.5), tupleScale(mask[y1][x1], 0.5))

    pic = npic

# convert to grayscale picture and show
im = Image.new("RGB", (len(pic[0]), len(pic)))

for y in range(len(pic)):
    for x in range(len(pic[0])):
        im.putpixel((x, y), tuple(map(int, pic[y][x])))

# Generate a name which encodes the hex vals of the mask
name = "tileart_"
for x in range(len(mask)):
    name += "["
    for y in range(len(mask[0])):
        name += "{:02x}{:02x}{:02x}".format(mask[x][y][0], mask[x][y][1], mask[x][y][2]) + ("," if y != len(mask[0]) - 1 else "")
    name += "]" + ("," if x != len(mask) - 1 else "")
name += "_" + "x" + str(iterations) + ".png"
im.save(name)
im.show()
