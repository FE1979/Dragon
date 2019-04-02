import sys
import pathlib


def first_file_line():
    """ Generator yields first line of a each file
        in directory and subdirectories
    """

    def first_line(file_path):
        """ reads first line for a file """

        with open(file_path, 'r') as f:
            line = f.readline()

        return line

    path = pathlib.Path.cwd()
    file_list = path.rglob('*.*')

    for i in file_list:
        yield i, first_line(i)


for i in first_file_line():
    print(i)
