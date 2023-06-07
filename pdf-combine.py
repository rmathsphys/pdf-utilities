'''
Usage example:
In: pdf-combine.py [-o] example1.pdf example2.pdf ...
Out: combine-example1.pdf OR example1.pdf (if -o used)

Run from command-line
Concatenates multiple input PDFs.
At least 1 PDF must be specified.
Copies metadata from the first PDF by default
'''

import argparse
from pathlib import Path
from pypdf import PdfReader, PdfWriter

parser = argparse.ArgumentParser(description='Combine multiple PDF files into a single one',
                    epilog='Example: pdf-combine -o test1.pdf test2.pdf ...')
parser.add_argument('infiles', action='append', nargs='+', help='List of PDFs to be combined (in order)')
parser.add_argument('--overwrite', '-o', action='store_true', help='Overwites the first file provided')

args = parser.parse_args()

flat_infiles = [j for i in args.infiles for j in i]

if len(flat_infiles) == 1:
    print('Only one source provided. Nothing to combine.')
    exit()

writer = PdfWriter()

# SETUP I/O
for j in range(len(flat_infiles)):
    pdf_path = Path(flat_infiles[j])
    
    if not pdf_path.is_file():
        print(f'Error: "{flat_infiles[j]}" could not be loaded!')
        exit()

    reader = PdfReader(pdf_path)

    if j == 0:
        metadata = reader.metadata
        writer.add_metadata(reader.metadata)

        if args.overwrite:
            outfile = f'{pdf_path.name}'
        else:
            outfile = f'combine-{pdf_path.name}'

    for page in reader.pages:
        writer.add_page(page)

# EXPORT PDF
with open(outfile, 'wb') as out:
    writer.write(out)

print(f'Succesfully exported to {outfile}')
