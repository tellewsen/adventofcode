import os
import pathlib
import requests


def download_input(year, day) -> str:
    session_cookie = os.environ["AOC_COOKIE"]
    session = requests.Session()
    session.cookies["session"] = session_cookie
    resp = session.get(url=f"https://adventofcode.com/{year}/day/{day}/input")
    return resp.text


def get_input(inputs_dir: pathlib.Path, year: str, day: str) -> str:
    filepath = pathlib.Path(inputs_dir) / pathlib.Path(year, f"{day}.txt")
    try:
        with open(filepath, "r") as f:
            return f.read()
    except FileNotFoundError:
        myinput = download_input(year, day)
        with open(filepath, "w") as f:
            f.write(myinput)
        return myinput
