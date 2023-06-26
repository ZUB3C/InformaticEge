import os.path
from os import listdir
from os.path import isfile, join
import time
from pathlib import Path

from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

from fake_useragent import UserAgent

import pandas as pd


def get_category_by_id(category_id: int) -> dict:
    params = {"theme": category_id, "filter": "all", "page": 1}
    problem_data = {}
    for page in range(1, 100):
        print(f"Doing category={category_id}, page={page}")
        params["page"] = page
        try:
            response = requests.get(f"{BASE_URL}/test", params=params, headers=headers)
        except Exception as ex:
            raise Exception(ex)
        soup = BeautifulSoup(response.text, "html.parser")
        problem_cards = soup.find_all('div', class_="problem_container")
        if not problem_cards:
            return problem_data
        for card in problem_cards:
            problem_id = card.get("id").replace("problem_", "")
            pbody = card.find("div", class_="pbody")
            file_urls = [urljoin(BASE_URL, url.get("href")) for url in pbody.find_all("a", {"target": "_blank"})]
            # print(problem_id, file_urls)
            problem_data[problem_id] = file_urls
    return problem_data


def download_file(url: str, file_path: Path) -> None:
    try:
        response = requests.get(url)
    except Exception as ex:
        raise Exception(ex)
    with open(file_path, "wt", encoding="utf-8") as file:
        file.write(response.text)
    print(f"Downloaded {url} to {file_path}")


def download_xls_file(url: str, file_path: Path) -> None:
    try:
        response = requests.get(url, headers=headers)
    except Exception as ex:
        raise Exception(ex)
    with open(file_path, "wb") as file:
        file.write(response.content)
    print(f"Downloaded {url} to {file_path}")


def convert_xls_files_to_csv(directory_path: Path) -> None:
    xls_file_paths = [os.path.join(directory_path, f) for f in listdir(directory_path) if isfile(join(directory_path, f)) if Path(f).suffix == ".xls"]
    for xls_file_path in xls_file_paths:
        csv_file_path = xls_file_path.replace(".xls", ".csv")
        if not os.path.exists(csv_file_path):
            read_file = pd.read_excel(xls_file_path)
            read_file.to_csv(csv_file_path, index=None, header=False)
        else:
            print(f"File {csv_file_path} already exists.")


if __name__ == '__main__':
    start_time = time.perf_counter()

    headers = {
        "user-agent": UserAgent().random
    }

    BASE_URL = "https://inf-ege.sdamgia.ru"
    categories = {
        "type_24": 413,  # Type 24
        "type_26": 415,  # Type 26
        "type_27": 416,  # Type 27
        "type_22": 215,  # Type 22
    }
    txt_files_categories = [413, 415, 416]
    xls_files_categories = [215]
    problem_ids_with_files = {}
    root = Path(__file__).parent
    for category_dir, category_id in categories.items():
        category_files_data = get_category_by_id(category_id)
        category_dir_path = os.path.join(root, category_dir)
        if not os.path.exists(category_dir_path):
            os.mkdir(category_dir_path)
        category_files_path = os.path.join(category_dir_path, "files")
        if not os.path.exists(category_files_path):
            os.mkdir(category_files_path)
        for problem_id, urls in category_files_data.items():
            if category_id in txt_files_categories:
                if len(urls) == 1:
                    file_path = os.path.join(category_files_path, f"{problem_id}.txt")
                    if not os.path.exists(file_path):
                        download_file(urls[0], file_path)
                    else:
                        print(f"File {file_path} already exists.")
                elif len(urls) == 2:
                    first_file_path = os.path.join(category_files_path, f"{problem_id}_A.txt")
                    if not os.path.exists(first_file_path):
                        download_file(urls[0], first_file_path)
                    else:
                        print(f"File {first_file_path} already exists.")
                    second_file_path = os.path.join(category_files_path, f"{problem_id}_B.txt")
                    if not os.path.exists(second_file_path):
                        download_file(urls[1], second_file_path)
                    else:
                        print(f"File {second_file_path} already exists.")
                else:
                    print(f"Expected 1 or 2 file urls, got {len(urls)}. {problem_id=}, {urls=}")
            elif category_id in xls_files_categories:
                file_path = os.path.join(category_files_path, f"{problem_id}.xls")
                if not os.path.exists(file_path):
                    download_xls_file(urls[0], file_path)
                else:
                    print(f"File {file_path} already exists.")
                convert_xls_files_to_csv(os.path.join(root, category_dir, "files"))
    print(f"Downloading took {round(time.perf_counter() - start_time, 3)} seconds.")
