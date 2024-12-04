import argparse
import importlib

import aoclib

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-y', '--year')
    parser.add_argument('-d', '--day')
    args = parser.parse_args()
    mod = importlib.import_module(f'{args.year}.{args.day}')
    myinput = aoclib.get_input(args.year, args.day) 
    mod.solver(myinput)
