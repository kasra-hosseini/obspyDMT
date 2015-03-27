from setuptools import setup
#from distutils.core import setup

setup(
    name="obspyDMT",
    version="0.9.9",
    description="obspyDMT: A Python Toolbox for Retrieving and Processing of Large Seismological Datasets",
    author="Kasra Hosseini",
    author_email="hosseini@geophysik.uni-muenchen.de",
    url="https://github.com/kasra-hosseini/obspyDMT",
    download_url="https://github.com/kasra-hosseini/obspyDMT.git",
    keywords=["obspyDMT", "ObsPy", "Seismology"],
    packages=["obspyDMT", "obspyDMT.utils"],
    requires=['matplotlib', 'numpy'],
    entry_points={
        'console_scripts': [
            'obspyDMT = obspyDMT.obspyDMT:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    long_description="""\
obspyDMT (obspy Data Management Tool) is a command line tool for retrieving,
processing and management of large seismological datasets in a fully automatic
way which can be run in serial or in parallel.
"""
)
