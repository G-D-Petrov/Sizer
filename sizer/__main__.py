import argparse
import logging
from sizer import convert_size, files_in_folder


def parse_args():
    parser = argparse.ArgumentParser(
                    prog = 'Sizer',
                    description = 'Recursively return all of the files in a given directory sorted by size')
    parser.add_argument('-p', '--path', help='Path to directory', required=True)
    parser.add_argument('-o', '--order', help='Order for sorting, defaults to Descending', default="Descending")
    parser.add_argument('--head', help='Option to specify how many entries you want to list, defaults to 10', default=10, type=int)
    parser.add_argument('-mr', "--machine_readable", help='Option to specify if the size of the files should be left uncoverted to human readable format, defaults to False', default=False, action='store_true')
    parser.add_argument( '-log',
                     '--loglevel',
                     default='warning',
                     help='Provide logging level. Example --loglevel debug, default=warning' )

    return parser.parse_args() 

if __name__ == '__main__':
    args = parse_args()  # <- command line arguments parsing
    logging.basicConfig( level=args.loglevel.upper() )
    logging.info( 'Logging now setup.' )
    file_sizes = files_in_folder(args.path, args.order)
    
    for size, filepath in file_sizes[:args.head]:
        if not args.machine_readable:
            size = convert_size(size)
        print(f"{size}: {filepath}")
