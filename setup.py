#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.errors import DistutilsExecError, CompileError
from distutils.unixccompiler import UnixCCompiler
from distutils.ccompiler import CCompiler
import os
from setuptools import setup, find_packages
from setuptools.extension import Extension
from subprocess import Popen, PIPE
import sys
#from distutils.core import setup


# Monkey patch the compilers to treat Fortran files like C files.
CCompiler.language_map['.f90'] = "c"
UnixCCompiler.src_extensions.append(".f90")

# Hack to prevent build_ext from trying to append "init" to the export symbols.
class finallist(list):
    """
    copyright:
    The Instaseis Development Team (instaseis@googlegroups.com)
    """
    def append(self, object):
        return

class MyExtension(Extension):
    """
    copyright:
    The Instaseis Development Team (instaseis@googlegroups.com)
    """
    def __init__(self, *args, **kwargs):
        Extension.__init__(self, *args, **kwargs)
        self.export_symbols = finallist(self.export_symbols)

def get_libgfortran_dir():
    """
    Helper function returning the library directory of libgfortran. Useful
    on OSX where the C compiler oftentimes has no knowledge of the library
    directories of the Fortran compiler. I don't think it can do any harm on
    Linux.

    copyright:
    The Instaseis Development Team (instaseis@googlegroups.com)
    """
    for ending in [".3.dylib", ".dylib", ".3.so", ".so"]:
        try:
            p = Popen(['gfortran', "-print-file-name=libgfortran" + ending],
                      stdout=PIPE, stderr=PIPE)
            p.stderr.close()
            line = p.stdout.readline().decode().strip()
            p.stdout.close()
            if os.path.exists(line):
                return [os.path.dirname(line)]
        except:
            continue
        return []

def _compile(self, obj, src, ext, cc_args, extra_postargs, pp_opts):
    compiler_so = self.compiler_so
    if ext == ".f90":
        if sys.platform == 'darwin' or sys.platform == 'linux2':
            compiler_so = ["gfortran"]
            cc_args = ["-O", "-fPIC", "-c", "-ffree-form"]
    try:
        self.spawn(compiler_so + cc_args + [src, '-o', obj] +
                   extra_postargs)
    except DistutilsExecError as msg:
        raise CompileError(msg)
UnixCCompiler._compile = _compile


src = os.path.join('obspyDMT', 'src')
lib = MyExtension('obspyDMT',
                  libraries=["gfortran"],
                  library_dirs=get_libgfortran_dir(),
                  # Be careful with the order.
                  sources=[
                      os.path.join(src, "lanczos.f90"),
                  ])

setup_config = dict(
    name="obspyDMT",
    version="0.9.9e",
    keywords=["obspyDMT", "ObsPy", "Seismology"],
    requires=['matplotlib', 'numpy'],
    description="obspyDMT: A Python Toolbox for Retrieving and Processing of "
                "Large Seismological Datasets",
    long_description="""\
obspyDMT (obspy Data Management Tool) is a command line tool for retrieving,
processing and management of large seismological datasets in a fully automatic
way which can be run in serial or in parallel.
""",
    author=u"Kasra Hosseini",
    author_email="hosseini@geophysik.uni-muenchen.de",
    url="https://github.com/kasra-hosseini/obspyDMT",
    packages=find_packages(),
    license="GNU Lesser General Public License, Version 3",
    platforms="OS Independent",
    ext_package='obspyDMT.lib',
    ext_modules=[lib],
    # this is needed for "pip install instaseis==dev"
    download_url="https://github.com/kasra-hosseini/obspyDMT.git",
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: MacOS",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Physics"],
    entry_points={
        'console_scripts': [
            'obspyDMT = obspyDMT.obspyDMT:main',
        ],
    }
)

if __name__ == "__main__":
    setup(**setup_config)

    # Attempt to remove the mod files once again.
    for filename in ["lanczos.mod"]:
        try:
            os.remove(filename)
        except:
            pass
