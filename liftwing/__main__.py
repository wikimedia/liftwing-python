from pprint import pprint

from liftwing import __metadata__


def main():
    for model in __metadata__:
        pprint(model)


if __name__ == "__main__":
    main()
