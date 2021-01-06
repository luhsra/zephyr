import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-o', type=str)
parser.add_argument('obj_string', type=str)

args= parser.parse_args()
objs= args.obj_string.replace(';', ' ')

os.system('llvm-link-9  -S -o ' + args.o + ' ' + objs)
