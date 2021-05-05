#!/usr/bin/env python

from setuptools import setup


def read_contents(name):
    with open(name, "r") as fh:
        return fh.read()


requires = [
    'pygame'
]


setup(
    name=f"pyconways-{read_contents('VERSION')}",
    version=read_contents("VERSION"),
    description=read_contents("DESCRIPTION"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Development Status :: 2 - Pre-Alpha",
        "License :: Other/Proprietary License",
        "Natural Language :: English",
        "Operation System :: OS Independant",
    ],
    author="ProServ",
    author_email="neoghostz@gmail.com",
    license="proprietary",
    url="https://github.com/neoghostz/pyconways",
    py_modules=["pyconways"],
    package_dir={"": "pyconways"},
    install_requires=requires,
    zip_safe=False,
)
