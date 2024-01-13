import sys

from src.finder import Finder


def main():
    # a = "*/15 0 1,15 * 1-5"
    f = Finder(sys.argv[1],command=sys.argv[0])
    f.find_info()
    print(f)


if __name__ == "__main__":
    main()
