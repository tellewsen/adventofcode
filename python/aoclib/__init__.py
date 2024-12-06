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


def find_word_occurences_in_grid(grid: list[str], target="XMAS") -> int:
    m, n = len(grid), len(grid[0])
    total = 0
    for i in range(m):
        for j in range(n):
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    x, y = i, j
                    if dx == dy == 0:
                        continue
                    for letter in target:
                        if not 0 <= x < m or not 0 <= y < n:
                            break
                        if grid[x][y] != letter:
                            break
                        x += dx
                        y += dy
                    else:
                        total += 1
    return total
