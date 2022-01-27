# Bronze
from zipfile import ZipFile
from PIL import Image
from PIL import ImageColor
import os
import json

# with open("example_bronze.json", "r") as content:
#     data = json.load(content)

# s = ''

# for i in data:
#     a = 0
#     for x in i:
#         a += x
#     s += str(a)
# # print(s)
# # Silver


# def split_numbers(string):
#     array = string.split('\n\n')
#     for x in range(len(array)):
#         array[x] = array[x].replace('\n', '')
#     # composite_list = [array[x:x+4] for x in range(0, len(array), 4)]
#     return array


# nums = {}

# with open('individual_digits.txt', 'r') as f:
#     numbers = split_numbers(f.read())
#     for i in range(10):
#         nums[numbers[i]] = i


# with ZipFile('example_silver.zip', 'r') as my_zip:
#     my_zip.extractall('example_silver')

# texts = []

# for file_num in range(1, 201):
#     with open(f'example_silver/text{file_num}.txt', 'r') as f:
#         texts.append(f.read())

# sum_of_pairs = ''
# for i in texts:
#     sum_of_nums = 0
#     for hash in split_numbers(i):
#         sum_of_nums += nums[hash]
#     sum_of_pairs += str(sum_of_nums)
# print(sum_of_pairs)

# Gold

with ZipFile('example_gold.zip', 'r') as my_zip:
    my_zip.extractall('example_gold')

# with Image.open('example_gold/image1.png') as im:
#     print(im.getdata())
#     print(im.getcolors())
#     print(im.size)
# box = (1, 1, 1, 1)
# region = im.crop(box)
