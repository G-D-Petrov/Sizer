from pathlib import Path
import os
import math
from tqdm import tqdm
import argparse

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

parser = argparse.ArgumentParser(
                    prog = 'Sizer',
                    description = 'Recursively return all of the files in a given directory sorted by size')

parser.add_argument('-p', '--path', help='Path to directory', required=True)
parser.add_argument('-o', '--order', help='Order for sorting, defaults to Descending', default="Descending")
parser.add_argument('--head', help='Option to specify how many entries you want to list, defaults to 10', default=10, type=int)

args = parser.parse_args()  # <- command line arguments parsing

# iterate over files in
# that directory
files = list(Path(args.path).rglob('*'))
file_sizes = [(os.path.getsize(file), file) for file in tqdm(files)]

if "Descending" == args.order:
    file_sizes.sort(reverse=True)
else:
    file_sizes.sort()

for size, filepath in file_sizes[:args.head]:
    print(f"{convert_size(size)}: {filepath}")