PDF Utilities
=============

CLI based set of simple utility scripts for quickly manipulating PDFs. Written in Python.

# Dependencies.
All PDF handling is done using `pypdf` provided by [py-pdf/pypdf](https://github.com/py-pdf/pypdf).

# Usage.
**Rotating Pages.**
Rotate some pages in "example.pdf" by 180 degrees. Rotates all the pages if the range is not specified.
```
pdf-rotate.py example.pdf 180 1 3 5-8 11
```
Creates a new PDF by default. Use the `-o` flag to overwrite the input file.

**Deleting Pages.**
Delete the specified pages from "example.pdf". Doesn't delete any page if the range is not specified.
```
pdf-delete.py example.pdf 1 3 5-8 11
```
Creates a new PDF by default. Use the `-o` flag to overwrite the input file.

**Keeping Pages.**
Keep only the specified pages from "example.pdf". Keeps all the pages if the range is not specified.
```
pdf-keep.py example.pdf 180 1 3 5-8 11
```
Creates a new PDF by default. Use the `-o` flag to overwrite the input file.

**Rotating Pages.**
Combine all the specified pdf files into a single pdf, in the given order.
```
pdf-combine.py input1.pdf input2.pdf input3.pdf
```