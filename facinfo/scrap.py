from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd
from scholarly import scholarly
from tqdm import tqdm
from tqdm.contrib.logging import logging_redirect_tqdm

import logging

HEADERS = {
    'User-agent':
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}
FIELDS = ["name", "affiliation", "email_domain", "interests", "hindex", "citedby", "citedby5y", "homepage"]


def get_bu_faculty():
    logging.info("Getting BU faculty list...")
    url = "https://www.bu.edu/bioinformatics/people/faculty/"
    html = requests.get(url, headers=HEADERS).text
    soup = BeautifulSoup(html, 'lxml')

    table = soup.select_one("#post-146")
    fac_list = list(table.find_all("a"))
    fac_names = [row.get_text() for row in fac_list]
    logging.info(f"...Obtained {len(fac_names)} faculty members!")
    return fac_names


def get_mit_meche_faculty():
    logging.info("Getting MIT MECHE faculty...")
    url = "http://meche.mit.edu/people"
    html = requests.get(url, headers=HEADERS).text
    soup = BeautifulSoup(html, 'lxml')

    fac_list = list(soup.find_all("div", class_="vc-child"))
    fac_names = [row.select_one("span").get_text() for row in fac_list[1:]]
    logging.info(f"...Obtained {len(fac_names)} faculty members!")
    return fac_names


def get_faculty_list(university):
    if university == "BU":
        return get_bu_faculty()
    if university == "MIT":
        return get_mit_meche_faculty()
    raise ValueError(f"University {university} not valid. Available are BU and MIT")


def get_author_details(name):
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
        except:
            field_val = None
        result[field] = field_val

    result["max_pub"] = author["publications"][0]["num_citations"]
    result["pub>1000"] = sum([pub["num_citations"]>1000 for pub in author["publications"]])

    return result


def scrap(university="BU"):
    faculty = get_faculty_list(university=university)

    results = {}
    with logging_redirect_tqdm():
        for fac_name in tqdm(faculty, position=0, leave=True):
            fac_info = get_author_details(fac_name)
            results[fac_name] = fac_info

    results = pd.DataFrame(results).T
    return results






