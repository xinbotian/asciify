from PIL import Image
import argparse

def get_char(r,g,b,alpha = 256):
    if alpha == 0:
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]
