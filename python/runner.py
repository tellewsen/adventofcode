import argparse
import importlib
import sys
import os
import pathlib
import dotenv

import aoclib

if __name__ == "__main__":
    dotenv.load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument("year", type=int)
    parser.add_argument("day", type=int)
    parser.add_argument("-p", action="store_true")
    args = parser.parse_args()
    year = str(args.year)
    day = str(args.day)
    try:
        mod = importlib.import_module(f"{year}.{day}")
    except ModuleNotFoundError:
        print(f"No solution function created for day {day} of {year}")
        sys.exit(1)
    myinput = aoclib.get_input(
        inputs_dir=pathlib.Path(os.path.realpath(__file__)).parent.parent
        / pathlib.Path("inputs"),
        year=year,
        day=day,
    )
    if args.p:
        print(f"Input: {myinput}")
    answers = mod.solver(myinput)
    try:
        # Old style that didn't print solutions underway
        if answers is not None:
            print(f"Part1: {answers[0]}")
            print(f"Part2: {answers[1]}")
    except Exception:
        # New style that does its own printing
        pass
