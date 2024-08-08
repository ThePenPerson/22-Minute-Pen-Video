from PIL import Image, ImageColor
from math import sqrt
import time

file = open(r"video data.txt","w+")
letters = open(r"Letters.txt","r")
letter_data = letters.read()
letter_list = letter_data.replace('\n', ' ').split(" ")
colours = open(r"Colours.txt","r")
colour_data = colours.read()
colour_list = colour_data.replace('\n', ' ').split(" ")


def hex_to_rgb(hex):
    return ImageColor.getcolor(hex, "RGB")

COLORS = []
for x in range(10):
    COLORS.append(hex_to_rgb(colour_list[x]))

def rgb_to_hex(red, green, blue):
    """Return color as #rrggbb for the given color values."""
    return '#%02x%02x%02x' % (red, green, blue)
    
def closest_color(rgb):
    r, g, b = rgb
    color_diffs = []
    for color in COLORS:
        cr, cg, cb = color
        color_diff = sqrt((r - cr)**2 + (g - cg)**2 + (b - cb)**2)
        color_diffs.append((color_diff, color))
    return min(color_diffs)[1]

#creates the dictionary of colours to use
hex_to_letter_dir = {}
for x in range(10):
    current_c = colour_list[x]
    hex_to_letter_dir[str(current_c)] = str(letter_list[x])


def scan(count):
    image = Image.open("out/output_1.jpg")
    
    y = 0
    x = 0
    for a in range(0, 4320):
        for b in range(0, 7680):
            
            rgb = image.getpixel((x, y))
            n_rgb = closest_color(rgb)
            hex_value = rgb_to_hex(n_rgb[0], n_rgb[1], n_rgb[2])
            letter = hex_to_letter_dir[str(hex_value)]
            file.write(letter)
            x += 1
        y += 1
        x = 0
        


scan(1)


file.close()
letters.close()
colours.close()