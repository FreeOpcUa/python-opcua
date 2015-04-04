from distutils.core import setup
from distutils.command.install_data import install_data


setup (name = "freeopcua", 
        version = "0.8.0",
        description = "Pure Python OPC-UA client and server library",
        author = "Olivier Roulet-Dubonnet",
        author_email = "olivier.roulet@gmail.com",
        url = 'http://freeopcua.github.io/',
        packages = ["opcua"],
        provides = ["opcua"],
        license = "GNU General Public License v3",

        classifiers = [
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "Operating System :: OS Independent",
            "Topic :: Software Development :: Libraries :: Python Modules",
        ]
        )


