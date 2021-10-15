# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

_MAJOR = 0
_MINOR = 2
_MICRO = 0
version = '%d.%d.%d' % (_MAJOR, _MINOR, _MICRO)
release = '%d.%d' % (_MAJOR, _MINOR)

metainfo = {
    'authors': {
        'Cokelaer': ('Thomas Cokelaer', 'thomas.cokelaer@pasteur.fr'),
        },
    'version': version,
    'license': 'BSD',
    'download_url': 'http://pypi.python.org/pypi/biosniff',
    'url': 'http://pypi.python.org/pypi/biosniff',
    'description': 'A sniffer for biological data formats',
    'platforms': ['Linux', 'Unix', 'MacOsX', 'Windows'],
    "keywords": ["NGS"],
    'classifiers': [
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Scientific/Engineering :: Bio-Informatics',
          'Topic :: Scientific/Engineering :: Information Analysis',]
    }


with open('README.rst') as f:
    readme = f.read()

requirements = open("requirements.txt").read().split()


setup(
    name='biosniff',
    version=version,
    maintainer=metainfo['authors']['Cokelaer'][0],
    maintainer_email=metainfo['authors']['Cokelaer'][1],
    author='The bioconvert Contributors',
    author_email=metainfo['authors']['Cokelaer'][1],
    long_description=readme,
    long_description_content_type='text/x-rst',
    keywords=metainfo['keywords'],
    description=metainfo['description'],
    license=metainfo['license'],
    platforms=metainfo['platforms'],
    url=metainfo['url'],
    download_url=metainfo['download_url'],
    classifiers=metainfo['classifiers'],
    zip_safe=False,
    packages=find_packages(),
    install_requires=requirements,

    # This is recursive include of data files
    exclude_package_data={"": ["__pycache__"]},

    package_data={
        },

    entry_points={
        'console_scripts': [
           'biosniff=biosniff.main:sniffer'
        ]
    }
    )
