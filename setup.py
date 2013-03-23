from setuptools import setup
#from distutils.core import setup

setup(
    name = "obspyDMT",
    version = "0.4.0",
    description = "Retrieving, Processing and Management of Massive Seismic Data (Serial and Parallel)",
    author = "Kasra Hosseini",
    author_email = "hosseini@geophysik.uni-muenchen.de",
    url = "https://github.com/kasra-hosseini/obspyDMT",
    download_url = "https://github.com/kasra-hosseini/obspyDMT.git",
    keywords = ["obspyDMT", "ObsPy", "Seismology"],
    packages=["obspyDMT"],
    entry_points = {
        'console_scripts': [
            'obspyDMT = obspyDMT.obspyDMT:main',
            'compareDMT = obspyDMT.compareDMT:main',
            'obspyDMT_managing_node = obspyDMT.obspyDMT_managing_node:main',
            'obspyNC = obspyDMT.obspyNC:main',
        ],
    },
    classifiers = [
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    long_description = """\
obspyDMT (ObsPy Data Management Tool) is a command line tool for retrieving, 
processing and management of massive seismic data in a fully automatic way 
which could be run in serial or in parallel. 
Moreover, complementary processing and managing tools have been 
designed and introduced in addition to the obspyDMT options. 
Because of the modular nature, different functionalities could be added 
easily and/or each obspyDMT can be used as a module for other programs.
"""
)
