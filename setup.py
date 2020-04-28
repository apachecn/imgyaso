#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import setuptools
import imgyaso

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    install_requires = fh.read().splitlines()

setuptools.setup(
    name="imgyaso",
    version=imgyaso.__version__,
    url="https://github.com/apachecn/imgyaso",
    author=imgyaso.__author__,
    author_email=imgyaso.__email__,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: Other/Proprietary License",
        "Natural Language :: Chinese (Simplified)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Utilities",
    ],
    description="提供多种图片有损压缩方式，包括自适应二值化、网格仿色、颜色缩减",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[
        "image",
        "processing",
        "lossy",
        "compression",
        "adaptive",
        "threshold",
        "bilevel",
        "grid",
        "dither",
        "quantize",
        "图像处理",
        "有损压缩",
        "自适应阈值",
        "二值化",
        "网格仿色",
        "颜色缩减",
    ],
    install_requires=install_requires,
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "imgyaso=imgyaso.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
)
