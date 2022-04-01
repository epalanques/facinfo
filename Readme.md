# Facinfo

This is a simple package that extracts information about faculty members and returns it
in a tabular form.

### Installation

The best way to install is to use with pip from git:
```shell script
pip install git+https://github.com/epalanques/facinfo.git
```

### Usage

#### From the shell
To see the possible arguments:
```shell script
facinfo --help
```
For example:
```shell script
facinfo BU --output Documents/BU_faculty.csv
```

#### From python

Just import and use
```python
from facinfo import scrap
fac_df = scrap(university="BU")
fac_df
```
