#!/usr/bin/python3
import argparse
import sys
import subprocess as sp
from pathlib import Path
import os

PWD = Path(sys.argv[0]).parent.resolve()

def parse_args():
    parser = argparse.ArgumentParser(description='run regressions parallelly by pushing one button.')
    parser.add_argument('-i', '--include', nargs='?', default='.*',
                        help='A regular expression. Only test cases matching this pattern will be run. [default: ".*"]')
    parser.add_argument('-e', '--exclude', nargs='?', default='^$',
                        help='A regular expression. Test cases matching this pattern will not be run. [default: "^$"]')
    args = parser.parse_args()
    return args

def all_test_executables():
    return PWD.joinpath('test').glob('*_test.py')

if __name__ == '__main__':
    args = parse_args()
    executables = all_test_executables()
    cmd = [
        '{}'.format(PWD.joinpath('testa/runtests.py')),
        '--lang', '{}'.format(PWD.joinpath('testa/lang.config')),
        '--dir', 'tres',
    ]
    if args.include:
        cmd.extend(['--include', args.include])
    if args.exclude:
        cmd.extend(['--exclude', args.exclude])
    cmd.extend('{}'.format(x.relative_to(PWD)) for x in executables)
    env = os.environ.copy()
    pypath = [
        PWD.joinpath('testa/python/').absolute(),
        PWD.joinpath('src/').absolute(),
    ]
    pypath = ':'.join("{}".format(x) for x in pypath)
    if 'PYTHONPATH' not in env:
        env['PYTHONPATH'] = pypath
    else:
        env['PYTHONPATH'] = '{}:{}'.format(env['PYTHONPATH'], pypath)
    sp.check_call(cmd, cwd=PWD, env=env)
