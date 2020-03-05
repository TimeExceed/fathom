# -*- python -*-
Import('env')

env.Install(
    '$BUILD_DIR/test',
    '#testa/python/testa.py')
env.Install(
    '$BUILD_DIR/test/',
    env.Glob('#src/*.py'))
