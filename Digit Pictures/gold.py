# Gold
from zipfile import ZipFile
from PIL import Image

# 2 methods:
# im.load()[0, 1]
# im.getpixel((0, 1))


def parse_image(px):
    num = []
    for x in range(3):
        for y in range(5):
            num.append(px[x, y])
    return num


nums = {}


def load_digits():
    for i in range(10):
        with Image.open(f'gold_digits/digit{i}.png') as im:
            px = im.load()
            num = parse_image(px)
            nums[tuple(num)] = i


with ZipFile('example_gold.zip', 'r') as my_zip:
    my_zip.extractall('example_gold')


with ZipFile('gold_digits.zip', 'r') as my_zip:
    my_zip.extractall('gold_digits')
    load_digits()

ans = ''

for i in range(1, 201):
    with Image.open(f'example_gold/image{i}.png') as im:
        px = im.load()
        num1 = []
        num2 = []

        for x in range(0, 3):
            for y in range(5):
                num1.append(px[x, y])

        for x in range(4, 7):
            for y in range(5):
                num2.append(px[x, y])

        num1 = nums[tuple(num1)]
        num2 = nums[tuple(num2)]
        ans += str(num1 + num2)

print(ans)
