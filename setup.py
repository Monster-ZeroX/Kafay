#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" setup.py for kafy.

https://github.com/SenuGamerBoy/Kafay

python setup.py sdist bdist_wheel

"""

from setuptools import setup
from kafy import __version__

setup(
    name='kafy',
    packages=['kafy'],
    scripts=['scripts/ytdl'],
    version=__version__,
    description="Retrieve YouTube content and metadata",
    keywords=["kafy", "API", "YouTube", "youtube", "download", "video"],
    author="SenuGamerBoy",
    author_email="shamilasamarakoon14@gmail@gmail.com",
    url="https://github.com/SenuGamerBoy/Kafay/",
    download_url="https://github.com/SenuGamerBoy/Kafay/tags",
    extras_require={
        'youtube-dl-backend': ["youtube-dl"],
        },
    package_data={"": ["LICENSE", "README.rst", "CHANGELOG", "AUTHORS"]},
    include_package_data=True,
    license='LGPLv3',
    classifiers=[
        "License :: OSI Approved :: GNU Lesser General Public License v3 "
        "(LGPLv3)",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Operating System :: MacOS :: MacOS 9",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft",
        "Operating System :: Microsoft :: Windows :: Windows 7",
        "Operating System :: Microsoft :: Windows :: Windows XP",
        "Operating System :: Microsoft :: Windows :: Windows Vista",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Intended Audience :: Developers",
        "Development Status :: 5 - Production/Stable",
        "Topic :: Multimedia :: Sound/Audio :: Capture/Recording",
        "Topic :: Utilities",
        "Topic :: Multimedia :: Video",
        "Topic :: Internet :: WWW/HTTP"],
    long_description=open("README.rst").read()
)
