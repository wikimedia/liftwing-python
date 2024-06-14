from liftwing import __metadata__
from pprint import pprint


def main():
    for model in __metadata__:
        pprint(model)


if __name__ == "__main__":
    main()
