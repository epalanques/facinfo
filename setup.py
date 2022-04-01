# Imports: third party
import toml
from setuptools import setup, find_packages

# Imports: first party
from facinfo import __DESCRIPTION__, __author__, __version__, __copyright__

with open("Pipfile", "r") as _pipfile:
    _PIPFILE_CONTENTS = toml.load(_pipfile)

setup(
    name="FacInfo",
    version=__version__,
    author=__author__,
    author_email="eric.palanques@gmail.com",
    license=__copyright__,
    description=__DESCRIPTION__,
    long_description=__DESCRIPTION__,
    url="https://github.com/epalanques/facinfo",
    packages=find_packages(
        exclude=[],
    ),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "facinfo = facinfo.scrap:main",
        ],
    },
    data_files=[(".", ["Pipfile"])],
    install_requires=list(_PIPFILE_CONTENTS["packages"].keys()),
)
