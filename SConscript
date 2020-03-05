# -*- python -*-
Import('env')

env.Install(
    '$BUILD_DIR/',
    '#testa/python/testa.py')
env.Install(
    '$BUILD_DIR/',
    env.Glob('#src/*.py'))
env.Install(
    '$BUILD_DIR/',
    env.Glob('#test/*.py'))
