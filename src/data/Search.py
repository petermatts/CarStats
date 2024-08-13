import argparse
import os
import re

def _getAttrs() -> list[str]:
    with open("../../Docs/Base.csv") as f:
        attributes = f.readline()

    return attributes.rstrip().split(",")


def makeArgs() -> tuple[dict[str, str], dict[str, str]]:
    description = """""" # todo write helpful description
    parser = argparse.ArgumentParser(description=description)
    attributes = _getAttrs()

    keymap = dict() # maps the keys to the right attribute name in the CSV

    seen = list()
    for attr in attributes:
        a = re.sub(r"@|ï¿½ |:|-|/|'|\(|\)", "", attr).lower()
        #? remove mulitple occurences of the same word (first occurence of duplicates)
        a = re.sub(r"\s+", "-", a)

        if a in seen:
            continue
        else:
            seen.append(a)

        parser.add_argument(f"--{a}", type=str)
        keymap[a.replace("-", "_")] = attr

    return vars(parser.parse_args()), keymap


def search(args: dict[str, str], keymap: dict[str,  str]) -> list:
    pass


if __name__ == "__main__":
    args, keymap = makeArgs()
    search(args, keymap)
