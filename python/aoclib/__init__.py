import pathlib

def download_input(year, day):
    with open():
        ...

def get_input(year, day):
    try:
        with open(pathlib.Path(year,day, '.txt'),'r') as f:
            return f.read()
    except:
        myinput = download_input(year, day)
        with open(pathlib.Path(year,day, '.txt'), 'w') as f:
            f.write(myinput)
        return myinput