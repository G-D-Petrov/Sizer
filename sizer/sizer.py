from pathlib import Path
import os
import math
from tqdm import tqdm
import logging

def convert_size(size_bytes: int) -> str:
    '''
        Converts input of raw number of bytes to humab readable format
        Example: 
            Input: 1024 byte
            Output: 1 KB
        Source: https://stackoverflow.com/a/14822210/10316860
    '''
    if size_bytes == 0:
        return "0 B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"

def get_size(file: Path) -> int:
    try:
        return os.path.getsize(file)
    except FileNotFoundError as ex:
        logging.info("A file was removed while the script was running, probably a temporary file")
        logging.info(ex)

    return 0

def files_in_folder(path: str, order: str) -> list():
    files = list(Path(path).rglob('*'))
    try:
        file_sizes = [(get_size(file), file) for file in tqdm(files)]
    except FileNotFoundError as ex:
        logging.info("A file was removed while the script was running, probably a temporary file")
        logging.info(ex)

    if "Descending" == order:
        file_sizes.sort(reverse=True)
    else:
        file_sizes.sort()

    return file_sizes