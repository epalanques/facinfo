# Imports: third party
from setuptools import setup, find_packages

# Imports: first party
from facinfo import __DESCRIPTION__, __author__, __version__, __copyright__

# pylint: disable-all

setup(
    name="facinfo",
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
            "facinfo = facinfo.entry:main",
        ],
    },
    data_files=[(".", ["Pipfile"])],
    install_requires=[
        "alabaster==0.7.12",
        "arrow==1.2.2",
        "async-generator==1.10",
        "attrs==21.4.0",
        "babel==2.9.1",
        "beautifulsoup4==4.10.0",
        "bibtexparser==1.2.0",
        "bs4==0.0.1",
        "certifi==2021.10.8",
        "cffi==1.15.0",
        "charset-normalizer==2.0.12; python_version >= '3'",
        "cryptography==36.0.2",
        "deprecated==1.2.13",
        "docutils==0.17.1",
        "fake-useragent==0.1.11",
        "free-proxy==1.0.6",
        "future==0.18.2",
        "h11==0.13.0",
        "idna==3.3; python_version >= '3'",
        "imagesize==1.3.0",
        "importlib-metadata==4.11.3; python_version < '3.10'",
        "jinja2==3.1.1",
        "lxml==4.8.0",
        "markupsafe==2.1.1",
        "numpy==1.22.3; platform_machine != 'aarch64' and platform_machine != 'arm64' and python_version < '3.10'",
        "outcome==1.1.0",
        "packaging==21.3",
        "pandas==1.4.1",
        "pycparser==2.21",
        "pygments==2.11.2",
        "pyopenssl==22.0.0",
        "pyparsing==3.0.7",
        "pysocks==1.7.1",
        "python-dateutil==2.8.2",
        "python-dotenv==0.20.0",
        "pytz==2022.1",
        "requests[socks]==2.27.1",
        "scholarly==1.6.0",
        "selenium==4.1.3",
        "six==1.16.0",
        "sniffio==1.2.0",
        "snowballstemmer==2.2.0",
        "sortedcontainers==2.4.0",
        "soupsieve==2.3.1",
        "sphinx==4.5.0",
        "sphinx-rtd-theme==1.0.0",
        "sphinxcontrib-applehelp==1.0.2",
        "sphinxcontrib-devhelp==1.0.2",
        "sphinxcontrib-htmlhelp==2.0.0",
        "sphinxcontrib-jsmath==1.0.1",
        "sphinxcontrib-qthelp==1.0.3",
        "sphinxcontrib-serializinghtml==1.1.5",
        "tqdm==4.63.1",
        "trio==0.20.0",
        "trio-websocket==0.9.2",
        "typing-extensions==4.1.1",
        "urllib3[secure,socks]==1.26.9",
        "wrapt==1.14.0",
        "wsproto==1.1.0",
        "zipp==3.7.0",
    ],
)
