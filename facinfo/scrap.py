# Imports: standard library
import logging
from typing import List

# Imports: third party
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from scholarly import scholarly
from tqdm.contrib.logging import logging_redirect_tqdm

HEADERS = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 "
    "Edge/18.19582",
}
FIELDS = [
    "name",
    "affiliation",
    "email_domain",
    "interests",
    "hindex",
    "citedby",
    "citedby5y",
    "homepage",
]


def get_bu_faculty():
    """Returns faculty members from BU - bioinformatics"""
    logging.info("Getting BU faculty list...")
    url = "https://www.bu.edu/bioinformatics/people/faculty/"
    html = requests.get(url, headers=HEADERS).text
    soup = BeautifulSoup(html, "lxml")

    table = soup.select_one("#post-146")
    fac_list = list(table.find_all("a"))
    fac_names = [row.get_text() for row in fac_list]
    logging.info(f"...Obtained {len(fac_names)} faculty members!")
    return fac_names


def get_mit_meche_faculty() -> List[str]:
    """Returns faculty members from MIT - MECHE"""
    logging.info("Getting MIT MECHE faculty...")
    url = "http://meche.mit.edu/people"
    html = requests.get(url, headers=HEADERS).text
    soup = BeautifulSoup(html, "lxml")

    fac_list = list(soup.find_all("div", class_="vc-child"))
    fac_names = [row.select_one("span").get_text() for row in fac_list[1:]]
    logging.info(f"...Obtained {len(fac_names)} faculty members!")
    return fac_names


def get_faculty_list(university: str) -> List[str]:
    """Returns a list with the faculty names of a university"""
    if university == "BU":
        return get_bu_faculty()
    if university == "MIT":
        return get_mit_meche_faculty()
    raise ValueError(f"University {university} not valid. Available are BU and MIT")


def get_author_details(name: str):
    """
    Queries google scholar for a specific person
    and returns a dictionary with all the author details "
    """
    search_query = scholarly.search_author(name)
    try:
        first_auth = next(search_query)  # Grab the first author only
    except StopIteration:
        logging.warning(f"Author {name} was not found!")
        result = {field: np.nan for field in FIELDS}
        result["max_pub"] = np.nan
        result["pub>1000"] = np.nan
        return result

    author = scholarly.fill(first_auth, sections=["basics", "indices", "publications"])

    result = {}
    for field in FIELDS:
        try:
            field_val = author[field]
        except KeyError:
            field_val = None
        result[field] = field_val

    result["max_cit"] = author["publications"][0]["num_citations"]
    result["pub>1000"] = sum(
        [pub["num_citations"] > 1000 for pub in author["publications"]],
    )

    return result


def scrap(university="BU", max_n=None):
    """
    Main function. Returns a dataframe with
    information about all the factulty members of a university
    """
    faculty = get_faculty_list(university=university)
    if max_n is not None:
        faculty = faculty[:max_n]

    results = {}
    with logging_redirect_tqdm():
        for fac_name in tqdm(faculty, position=0, leave=True):
            fac_info = get_author_details(fac_name)
            results[fac_name] = fac_info

    results = pd.DataFrame(results).T
    return results
