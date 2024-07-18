import sys
import random
from PIL import Image

class TxtClr:
	red = '\033[91m'
	green = '\033[92m'
	blue = '\033[94m'
	reset = '\033[0m'

def clr(hexColor:str)->str:
	hexColor = [hexColor[i:i+2] for i in range(0, len(hexColor), 2)]
	return f"0x{TxtClr.red}{hexColor[0]}{TxtClr.green}{hexColor[1]}{TxtClr.blue}{hexColor[2]}{TxtClr.reset}"

def randomClr(max_tuples=3,max_clr=3)->str:
	num_tuples = random.randint(1, max_tuples)
	num_colors = random.randint(1, max_clr)
	colors = ""
	for i in range(num_tuples):
		color = []
		for j in range(num_colors):
			txt:str=clr(f"{random.randint(0x000000, 0xffffff):06x}")
			color.append(txt)
		end = "" if i == num_tuples - 1 else " "
		colors += f"\({','.join(color)}\){end}"
	return colors

if len(sys.argv) < 2:
	print(f"Usage: python {sys.argv[0]} <mask1> <mask2> ...")
	print(f"Example: python {sys.argv[0]} \(%s,%s\) \(%s,%s\)" % (clr("0000ff"), clr("ff0000"),clr("0000ff"), clr("ff0000")))
	print("\tWhere mask is an RGB value in hex format")
	print("")
	print("If you don't know what mask to use, try this one out:")
	print(f"\npython {sys.argv[0]} {randomClr()}")

	sys.exit(0)

mask = []*len(sys.argv)
for i in range(1, len(sys.argv)):
	mask.append([])
	rgb = sys.argv[i].replace("0x","").replace("(","").replace(")","").split(",")
	print(rgb)
	for j in range(len(rgb)):
		rgb[j] = tuple(rgb[j][i:i+2] for i in range(0, len(rgb[j]), 2))
		rgb[j] = tuple(map(lambda x: int(x, 16), rgb[j]))
		mask[i-1].append(rgb[j])
print(mask)
iterations = 3
pic = mask

def tupleScale(t, m):
	return tuple(map(lambda e: e * m, t))

def tupleAdd(a, b):
	return tuple((a[i] + b[i] for i in range(len(a))))

for i in range(iterations):
	# Square the pic
	npic = [[0 for _ in range(len(pic[0]) * len(mask[0]))] for _ in range(len(pic) * len(mask))]
	for y in range(len(pic)):
		for x in range(len(pic[0])):
			for y1 in range(len(mask)):
				for x1 in range(len(mask[0])):
					npic[y + y1 * len(pic)][x + x1 * len(pic[0])] = tupleAdd(tupleScale(pic[y][x], 0.5), tupleScale(mask[y1][x1], 0.5))

	pic = npic

# Convert to grayscale pic and show
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
