#! /bin/sh
#
# This script generates a .deb file for generating a debian package of python-opcua
# You need to install python-stdeb to use it.
# Usage : ./make_deb.sh
# The package is generate in ./deb_dist
#
python setup.py --command-packages=stdeb.command bdist_deb
