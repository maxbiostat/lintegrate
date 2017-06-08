#!/usr/bin/env python

from setuptools import setup, find_packages
from setuptools import Extension

import os, sys, numpy, re

ext_modules = [ Extension("lintegrate",
                          sources =[ "lintegrate.pyx", "../src/lintegrate_qag.c", "../src/lintegrate_qng.c", "../src/lintegrate_cquad.c"],
                          include_dirs=[numpy.get_include(), '.', os.popen('gsl-config --cflags').read()[2:-1], '../src'],
                          library_dirs=['.', os.popen('gsl-config --libs').read().split()[0][2:]],
                          libraries=['gsl', 'gslcblas'], extra_compile_args=['-O3', '-DHAVE_PYTHON_LINTEGRATE']) ]

# get version string for pyx file (see e.g. https://packaging.python.org/single_source_version/)
def find_version():
  fp = open('lintegrate.pyx', 'r')
  version_file = fp.read()
  fp.close()
  version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
  if version_match:
    return version_match.group(1)
  raise RuntimeError("Unable to find version string.")

setup(
  name = 'lintegrate',
  version = find_version(),
  url = 'https://github.com/mattpitkin/lintegrate',
  description = 'Python functions implementing numerical integration of functions in log-space.',
  author = 'Matthew Pitkin',
  author_email = 'matthew.pitkin@glasgow.ac.uk',
  packages = find_packages(),
  setup_requires = ['numpy'],
  install_requires = ['numpy', 'scipy', 'cython'],
  ext_modules = ext_modules,
  classifiers=[
      'Intended Audience :: Science/Research',
      'License :: OSI Approved :: GNU General Public License (GPL)',
      'Operating System :: POSIX :: Linux',
      'Programming Language :: Python',
      'Programming Language :: C',
      'Natural Language :: English'
      ]
)

