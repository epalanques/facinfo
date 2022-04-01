# Facinfo

This is a simple package that extracts information about a list of researchers
from google scholar and returns it in a tabular format.

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

#### Output
An example of the output:

|                      | name                          | affiliation                                                                       | email_domain             | interests                                                                                     |   hindex |   citedby |   citedby5y | homepage                                   |   max_cit |   pub>1000 |
|:---------------------|:------------------------------|:----------------------------------------------------------------------------------|:-------------------------|:----------------------------------------------------------------------------------------------|---------:|----------:|------------:|:-------------------------------------------|----------:|-----------:|
| Allen, Karen         | Karen N. Allen                | Chair and Professor, Department of Chemistry, Boston University                   | @bu.edu                  | ['enzyme mechanisms', 'X-ray crystallography', 'phosphoryl transfer', 'enzyme evolution']     |       44 |      6616 |        2390 | http://www.bu.edu/chemistry/faculty/allen/ |       410 |          0 |
| Belta, Calin         | Calin Belta                   | Professor, Boston University                                                      | @bu.edu                  | ['Controls', 'Formal Methods', 'Robotics', 'Systems Biology']                                 |       54 |     10835 |        5507 |                                            |       553 |          0 |
| Benson, Gary         | Gary Benson                   | Associate Professor, Computer Science, Bioinformatics, Biology, Boston University | @bu.edu                  | ['Pattern matching algorithms', 'sequence alignment', 'DNA sequence analysis', 'DNA repeats'] |       31 |     10402 |        3745 | http://tandem.bu.edu/home.html             |      6334 |          1 |
| Bhatnagar, Jennifer  | Jennifer M. Bhatnagar         | Assistant Professor of Microbial Ecology, Boston University                       | @bu.edu                  | ['Microbial ecology', 'ecosystem science', 'biogeochemistry']                                 |       25 |      3735 |        2705 | https://microbesatbu.wordpress.com/        |       484 |          0 |
| Bhattacharya, Dileep | Dr. Dilip Kumar Bhattacharyya | Professor of Microbiology,  Assam Agricultural University                         | @vetbifguwahati.ernet.in | ['Microbiology', 'Veterinary Science', 'Animal Science']                                      |       11 |       778 |         285 | http://bifguwahati.ernet.in/               |       142 |          0 |

The meaning of the columns is (information as appears in Google Scholar):
* Name: name if the faculty member as in Google Scholar
* Affiliation
* email_domain
* interests
* hindex
* citedby: cumulative number of citations
* citedby5: cumulative number of citations in the las 5 years
* homepage
* max_cit: publication with the maximum number of citations
* pub>1000: number of publications with more than 1000 citations
