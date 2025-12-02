from matplotlib import pyplot as plt

WIDTH = 25
HEIGHT = 6
data = open("input").read().strip()

image = []
layer = []
pixels = []
for i in range(0, len(data), WIDTH):
    pixels.append(data[i : i + WIDTH])
    if len(pixels) == HEIGHT:
        layer.extend(pixels)
        pixels = []
    if layer:
        image.append(layer)
        layer = []
least_zeros = None
for i in range(len(image)):
    foo = "".join((image[i]))
    if least_zeros is None:
        least_zeros = (i, foo.count("0"), foo.count("1") * foo.count("2"))
    else:
        count = foo.count("0")
        if least_zeros[1] > count:
            least_zeros = (i, count, foo.count("1") * foo.count("2"))
print("Part #1:", least_zeros[2])

processed = list("2" * WIDTH * HEIGHT)
for layer in image:
    layer = list("".join(layer))
    for i in range(len(layer)):
        if processed[i] == "2" and layer[i] != "2":
            processed[i] = layer[i]

image_done = [processed[i : i + WIDTH] for i in range(0, len(processed), WIDTH)]
print(image_done)
print("final image")
for i in range(HEIGHT):
    for j in range(WIDTH):
        image_done[i][j] = int(image_done[i][j])
plt.imshow(image_done)
plt.show()
