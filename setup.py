#!/usr/bin/env python

import io
import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py bdist_wheel sdist upload')
    sys.exit()

package_dir ={
    '': './',
    'colorama': './colorama',
    'jsbeautifier': './jsbeautifier',
    'jsontemplate': './jsontemplate',
    'ordlookup': './ordlookup',
    'pcapparser': './pcapparser',
    'plugins': './plugins',
    'storage': './storage',
}

packages = [
    '',
    'colorama',
    'jsbeautifier',
    'jsontemplate',
    'ordlookup',
    'pcapparser',
    'plugins',
    'storage',
]

data_files=[
    ('', ['LICENSE', 'magics.csv', 'userdb.txt']),
    ('jsontemplate', ['jsontemplate/CapTipperTemplate.html']),
    ('storage/fiddler2pcap', ['storage/fiddler2pcap/saz2pcap.sh']),
]

scripts=[
    'CapTipper.py',
]

with io.open('README.txt', encoding='utf-8') as f:
    readme = f.read()

with io.open('CHANGELOG', encoding='utf-8') as f:
    changelog = f.read()

setup(
    name='CapTipper',
    version='0.3',
    description='Malicious HTTP traffic explorer',
    long_description=readme + '\n\n' + changelog,
    author='omriher',
    author_email='omriher@gmail.com',
    maintainer='pigfoot',
    maintainer_email='pigfoot@gmail.com',
    url='https://captipper.readthedocs.org',
    package_dir=package_dir,
    packages=packages,
    data_files=data_files,
    scripts=scripts,
    include_package_data=True,
    license='GNU GPLv3',
    classifiers=(
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ),
)
