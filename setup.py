from setuptools import setup, find_packages

import sys
import re
from os import path


def translate_from_trollius_to_asyncio():
    pypaths = [
        ["client", "ua_client.py"],
    ]

    curdir = path.dirname(path.realpath(__file__))
    for pypath in pypaths:
        fpath = path.join(curdir, "opcua", *pypath)
        with open(fpath, 'r+b') as f:
            src = f.read()
            src = re.sub(br"raise Return\(\s*\)", b"return", src)
            src = re.sub(br"raise Return\(", b"return (", src)
            src = re.sub(br"yield From\(None\)", b"yield from []", src)
            src = re.sub(br"yield From\(", b"yield from (", src)
            f.seek(0)
            f.truncate(0)
            f.write(src)

if len(sys.argv) >= 2 and sys.argv[1] == "asyncio_translate":
    translate_from_trollius_to_asyncio()
    sys.exit()

install_requires = []
if sys.version_info[0] < 3 or sys.version_info[1] < 2:
    # python 2.7 - python 3.1
    install_requires.append("futures")
if sys.version_info[0] < 3 or sys.version_info[1] < 3:
    # python 2.7 - python 3.2
    install_requires.append("trollius")
else:
    translate_from_trollius_to_asyncio()
if sys.version_info[0] < 3 or sys.version_info[1] < 4:
    # python 2.7 - python 3.3
    install_requires.append("enum34")


setup(name="freeopcua", 
      version="0.10.7",
      description="Pure Python OPC-UA client and server library",
      author="Olivier Roulet-Dubonnet",
      author_email="olivier.roulet@gmail.com",
      url='http://freeopcua.github.io/',
      packages=find_packages(),
      provides=["opcua"],
      license="GNU Lesser General Public License v3 or later",
      install_requires=install_requires,
      extras_require={
          'encryption': ['cryptography']
      },
      classifiers=["Programming Language :: Python",
                   "Programming Language :: Python :: 3",
                   "Programming Language :: Python :: 2",
                   "Development Status :: 4 - Beta",
                   "Intended Audience :: Developers",
                   "Operating System :: OS Independent",
                   "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
                   "Topic :: Software Development :: Libraries :: Python Modules",
                   ],
      entry_points={'console_scripts':
                    [
                        'uaread = opcua.tools:uaread',
                        'uals = opcua.tools:uals',
                        'uabrowse = opcua.tools:uals',
                        'uawrite = opcua.tools:uawrite',
                        'uasubscribe = opcua.tools:uasubscribe',
                        'uahistoryread = opcua.tools:uahistoryread',
                        'uaclient = opcua.tools:uaclient',
                        'uaserver = opcua.tools:uaserver',
                        'uadiscover = opcua.tools:uadiscover'
                    ]
                    }
      )
