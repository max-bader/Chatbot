def grayscale(list):
    for a in list:
        for b in a:
            total = 0
            for c in b:
                total += c
                avg = int(total / 3)
            for i in range(len(b)):
                b[i] = avg
    return list
pixels = [[[0, 255, 0], [255, 0, 0]], [[0, 0, 255], [255, 255, 255]]]
print(grayscale(pixels))
