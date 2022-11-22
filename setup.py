# Copyright (c) Materials Virtual Lab
# Distributed under the terms of the Modified BSD License.

from setuptools import setup, find_namespace_packages

import os

SETUP_PTH = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(SETUP_PTH, "README.rst")) as f:
    desc = f.read()


setup(
    name="pymatgen-io-lammps",
    packages=find_namespace_packages(include=["pymatgen.io.*"]),
    version="0.0.1",
    install_requires=["pymatgen>=2022.0.3"],
    extras_require={},
    package_data={},
    author="Matgenix",
    author_email="contact@matgenix.com",
    maintainer="Matgenix",
    url="https://github.com/Matgenix/pymatgen-io-lammps",
    license="MIT",
    description="Add-on to pymatgen for lammps inputs/outputs and set generators.",
    long_description=desc,
    keywords=["lammps"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
