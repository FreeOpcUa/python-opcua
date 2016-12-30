from setuptools import setup, find_packages

import sys

if sys.version_info[0] < 3:
    install_requires = ["python-dateutil", "enum34", "trollius", "futures", "pytz"]
else:
    install_requires = ["python-dateutil", "pytz"]

setup(name="freeopcua",
      version="0.90.1",
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
                        'uadiscover = opcua.tools:uadiscover',
                        'uacall = opcua.tools:uacall',
                    ]
                    }
      )

