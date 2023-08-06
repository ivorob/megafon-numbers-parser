#!/usr/bin/env python

"""Setup file for megafon-numbers-parser."""
import setuptools

if __name__ == '__main__':
    try:
        setuptools.setup(setup_requires=['pbr'], pbr=True)
    except: # noqa
        print(
            "\n\nAn error occurred while building the project, "
            "please ensure you have the most updated version of setuptools "
            "and wheel with:\n"
            "    pip install -U setuptools wheel\n\n"
        )
        raise
