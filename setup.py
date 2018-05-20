#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="obspyDMT",
    version="2.1.1",
    keywords=["obspyDMT", "obspy", "seismology", "geophysics"],
    requires=['matplotlib', 'numpy'],
    description="obspyDMT: A Python Toolbox for Retrieving, Processing and "
                 "Management of Seismological Datasets",
    long_description="""\
obspyDMT (obspy Data Management Tool) is a command line tool for retrieving,
processing and management of seismological datasets in a fully automatic way.
""",
    author=u"Kasra Hosseini",
    author_email="kasra.hosseinizad@earth.ox.ac.uk",
    url="https://github.com/kasra-hosseini/obspyDMT",
    license="GNU Lesser General Public License, Version 3",
    platforms="OS Independent",
    packages=["obspyDMT", "obspyDMT.utils"],
    # this is needed for "pip install instaseis==dev"
    download_url="https://github.com/kasra-hosseini/obspyDMT/archive/master.zip",
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Operating System :: Unix",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Physics"],
    entry_points={
        'console_scripts': [
            'obspyDMT = obspyDMT.obspyDMT:main',
        ],
    }
)
