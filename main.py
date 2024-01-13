import sys

from src.finder import Finder


def main():
    # "*/15 0 1,15 * 1-5"
    finder = Finder(sys.argv[1],command=sys.argv[0])
    finder.find_info()
    print(finder)


if __name__ == "__main__":
    main()
