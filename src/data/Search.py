import argparse
import os

def _getAttrs() -> list[str]:
    with open("../../Docs/Base.csv") as f:
        attributes = f.readline()

    return attributes.rstrip().split(",")

def makeArgs():
    # todo, automatically configure args based on all attributes
    parser = argparse.ArgumentParser()
    attributes = _getAttrs()

    print(attributes)


if __name__ == "__main__":
    makeArgs()
