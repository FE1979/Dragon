import re
import sys
import argparse
import pathlib

parser = argparse.ArgumentParser(description="Reads text enclosed with tag",
                            usage="title.py [filename] [tag]")
parser.add_argument("filename", help="File title. Must be in same directory",
                    type=str)
parser.add_argument("tag", help="Tag w/out '<' or '>'. No closing tag is needed.",
                    type=str)

args = parser.parse_args()

path = pathlib.Path.cwd() / args.filename

tag = args.tag

if path.exists():
    tag_match = r"<" + tag + r">[\s\S]+</" + tag + r">"
    tag_len = len(tag)

    file_data = ""
    with open(path, 'r') as f:
         file_data = f.read()

    match = re.search(tag_match, file_data, flags=re.I)
    if match:
        print(match.string[match.start() + tag_len+2 : match.end() - tag_len-3])
    else:
        print('No tag found')

else:
    print("File doesn't exists")
