# -*- coding: utf-8 -*-
from setuptools import setup
from balderexample.loginserver import __version__

setup(
    name='balderexample-loginserver',
    version=__version__,
    author='Max Stahlschmidt',
    author_email='max@baldertest.com',
    package_dir={'': 'src'},
    packages=[
        "src/loginserver/loginserver",
        "src/loginserver/mainapp",
        "src/loginserver"
    ],
    url='todo',
    package_data={
        'static': [
            'src/loginserver/db.sqlite3',
            'src/balderexample/loginserver/mainapp/static/**/*'
        ],
    },
    license='LICENSE.txt',
    description='example project for balder testing and learning',
    long_description=open('README.md').read(),
    install_requires=[
        "Django>=4.0.2",
        "djangorestframework>=3.13.1"
    ],
    scripts=['scripts/balderexample-loginserver'],
    python_version=">=3.9"
)
