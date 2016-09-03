from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from fabric.api import (local, task, env)

env.use_ssh_config = True


@task
def build():
    '''Build wheel.'''
    local('''python setup.py sdist bdist_wheel''')


@task
def clean():
    '''Clean.'''
    local('''rm -rf *.pyc *.egg-info build dist''')


@task
def upload():
    build()
    local('''twine upload -s dist/*''')
