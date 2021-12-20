"""
The trick in this one is that the pixel switches if itself and all its neighbours are
the same. This means that the infinite area outside the original image will flash on
and off every step. To account for this we simply keep track of which step we are on,
and pad the surrounding area accordingly.
"""


def read_file(fname):
    with open(fname) as f:
        image = {}
        for i, line in enumerate(f.readlines()):
            if i == 0:
                algo = line.rstrip()
                continue
            for j, data in enumerate(line.rstrip()):
                image[(i-2, j)] = data
        return algo, image


def pad(image, step):
    pad_char = '.' if step % 2 == 0 else '#'
    min_x, min_y = min(k for k in image)
    max_x, max_y = max(k for k in image)
    padded = image.copy()
    # sides
    for y in range(min_y, max_y+1):
        padded[(min_x-1, y)] = pad_char
        padded[(max_x+1, y)] = pad_char
    # top bottom
    for x in range(min_x-1, max_x+2):
        padded[x, min_y-1] = pad_char
        padded[x, max_y+1] = pad_char
    return padded


def get_new_pixel(padded_image, point, algo):
    total = ''
    for i in get_neighbours(point):
        total += '1' if padded_image[i] == '#' else '0'
    return algo[int(total, 2)]


def build_new_img(image, padded_image, algo):
    new_img = {}
    for point in image:
        new_img[point] = get_new_pixel(padded_image, point, algo)
    return new_img


def solve(algo, image, step):
    image = pad(image, step)
    padded_image = pad(image, step)
    return build_new_img(image, padded_image, algo)


def get_neighbours(point):
    x, y = point
    neigs = []
    for i in [x-1, x, x+1]:
        for j in [y-1, y, y+1]:
            neigs.append((i, j))
    return neigs


def count_lights(image):
    return sum([1 for v in image.values() if v == '#'])


def main():
    algo, image = read_file('input.txt')

    for i in range(50):
        image = solve(algo, image, i)
        if i == 1:
            print(1, count_lights(image))
    print(2, count_lights(image))


main()
