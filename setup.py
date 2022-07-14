#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="obspyDMT",
    version="2.2.9",
    keywords=["obspyDMT", "obspy", "seismology", "geophysics"],
    description="obspyDMT: A Python Toolbox for Retrieving, Processing and "
                 "Management of Seismological Datasets",
    long_description="""\
obspyDMT (obspy Data Management Tool) is a command line tool for retrieving,
processing and management of seismological datasets in a fully automatic way.
""",
    author=u"Kasra Hosseini",
    author_email="k.hosseinizad@gmail.com",
    url="https://github.com/kasra-hosseini/obspyDMT",
    license="GNU Lesser General Public License, Version 3",
    platforms="OS Independent",
    packages=["obspyDMT", "obspyDMT.utils"],
    # this is needed for "pip install instaseis==dev"
    download_url="https://github.com/kasra-hosseini/obspyDMT/archive/master.zip",
    install_requires=[
        "obspy>=1.2.0,<2.0.0",
        "matplotlib>=3.2.0",
    ],
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
