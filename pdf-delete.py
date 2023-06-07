'''
Usage example:
In: pdf-delete.py example.pdf [-o] -r 1-3 5 7-9
Out: delete-example.pdf OR example.pdf [if -o used]

Run from command-line
Delete no pages if no range specified (default).
'''

import argparse
from pathlib import Path
from pypdf import PdfReader, PdfWriter

parser = argparse.ArgumentParser(description='Delete specified pages in a PDF',
                    epilog='Example: pdf-delete example.pdf -o -r 1-3 5 7-9')

parser.add_argument('infile', type=str, help='PDF file (eg. example.pdf)')
parser.add_argument('--ranges', '-r', action='append', default=[], nargs='*', help='Page numbers (eg. 1-3 5 7-9)')
parser.add_argument('--overwrite', '-o', action='store_true', help='Overwites the current file')

args = parser.parse_args()

# SETUP I/O
pdf_path = Path(args.infile)
if not pdf_path.is_file():
    print('Error locating this PDF file!')
    exit()

reader = PdfReader(pdf_path)
metadata = reader.metadata

name = pdf_path.name
outfile = f'{name}' if args.overwrite else f'delete-{name}'

writer = PdfWriter()

# SETUP RANGES (! negatives, backwards, zero)
if len(args.ranges) > 0:
    ranges = [j for i in args.ranges for j in i]
    ranges = [[int(y) for y in x.split('-')] for x in ranges]
    bucket = []
    for interval in ranges:
        bucket += list(range(interval[0]-1, interval[-1]))
else:
    print('Error: no range provided! Which pages do you want to delete?')
    exit()

# PERFORM DELETION
for pnum in range(len(reader.pages)):
    page = reader.pages[pnum]
    if pnum not in bucket:
        writer.add_page(page)

# EXPORT PDF
writer.add_metadata(reader.metadata)
with open(outfile, 'wb') as out:
    writer.write(out)
