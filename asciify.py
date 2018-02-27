from PIL import Image
import argparse

#command line input var
parser = argparse.ArgumentParser()

parser.add_argument('file') #input file
parser.add_argument('-o', '--output') #output file
parser.add_argument('--width', type = int, default= 80) #output width
parser.add_argument('--height', type = int, default = 80)# output height

#get var
args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
