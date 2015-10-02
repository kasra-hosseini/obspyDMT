#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="obspyDMT",
    version="1.0.0",
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
    license="GNU Lesser General Public License, Version 3",
    platforms="OS Independent",
    packages=["obspyDMT", "obspyDMT.utils"],
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
