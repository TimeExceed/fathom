#!/usr/bin/python3
import os.path as op
import subprocess as sp
import shutil as sh
from pathlib import Path

def print_help():
    print('Syntax: input.py output [ARGS]')
    print()
    print('input.py\tThe python program to draw the figure.')
    print('output\t\tThe output file. Supports all file formats which pdftocairo supports.')
    print('ARGS\t\tOptional args given to pdftocairo except format specifier like -png. File format is determined automatically by the output file\'s suffix .')

def parse_args():
    import sys
    if len(sys.argv) < 3:
        print_help()
        sys.exit(2)
    drawer = sys.argv[1]
    output = sys.argv[2]
    args = sys.argv[3:]
    return (drawer, output, args)

def determine_file_format(filename):
    _, ext = op.splitext(filename)
    assert ext
    return ext.replace('.', '')

def draw(drawer):
    work_dir = Path('/tmp/work')
    work_dir.mkdir(parents=True)
    with open(work_dir.joinpath('x.tex'), 'w') as fp:
        sp.run(['/usr/bin/python3', '-B', drawer],
               cwd='/opt/code',
               stdout=fp).check_returncode()
    sp.run(['lualatex', 'x.tex'],
           cwd=work_dir).check_returncode()
    return work_dir.joinpath('x.pdf')

def crop(inp):
    parent = inp.parent
    out = parent.joinpath('y.pdf')
    sp.run(['pdfcrop', inp.name, out.name],
           cwd=parent).check_returncode()
    return out

def convert(pdf, args):
    parent = pdf.parent
    files = set(x for x in parent.iterdir())
    sp.run(['/usr/bin/pdftocairo'] + args + [pdf.name],
           cwd=parent).check_returncode()
    new_files = set(x for x in parent.iterdir())
    out = new_files - files
    assert len(out) == 1, 'Too large a figure it is!'
    out = list(out)[0]
    return out

def copy_back(result, output):
    output = Path('/opt/code').joinpath(output)
    sh.copyfile(result, output)

if __name__ == '__main__':
    drawer, output, args = parse_args()
    file_format = determine_file_format(output)
    pdf = draw(drawer)
    pdf2 = crop(pdf)
    if file_format == 'pdf':
        out = pdf2
    else:
        args.append('-%s' % file_format)
        out = convert(pdf2, args)
    copy_back(out, output)


