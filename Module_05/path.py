"""
Demonstration script of pathlib
"""

import os
import re
import pathlib

path = pathlib.Path.cwd()
choice = ''
quit = False
file_list = []

cd = re.compile("^cd ")

while not quit:

    print(f'\nCurrent directory: \n{path}\n')
    choice = input("""Type U to move one level up, CD [dir] to change directory\n"""\
                    +"""DIR for list of files, DIRW for list of dir-es and Q for exit\n""")
    choice = choice.lower()

    if choice.lower() == 'u':
        """move up"""
        if len(list(path.parents)) > 0:
            os.chdir(list(path.parents)[0])
            path = pathlib.Path.cwd()
        pass

    elif cd.match(choice) is not None:
        "change dir"
        choice = cd.sub('', choice)
        path2 = path / choice
        if not path2.exists():
            print('\nPlease, type correct name of directory')
        else:
            path = path2
        pass

    elif choice.lower() == 'dir':
        "list all files"
        file_list = []

        for item in os.scandir(path):
            if item.is_file():
                file_list.append(item)

        print('\nList of files:')
        for item in file_list:
            print(item.name)
        pass

    elif choice.lower() == 'dirw':
        """ list directories """
        dir_list = []
        for item in os.scandir(path):
            if item.is_dir():
                dir_list.append(item)
        print('\nList of directories:')
        for item in dir_list:
            print(item.name)

    elif choice.lower() == 'q':
        quit = True


    else:
        print("\nPlease, type correct command.")
