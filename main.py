import sys

from src.finder import Finder


def main():
    # "*/15 0 1,15 * 1-5"
    sys_data = sys.argv[1].strip().split(" ")

    expression = " ".join(sys_data[:5])
    command = " ".join(sys_data[5:])
    finder = Finder(expression,command=command)
    finder.find_info()
    print(finder)


if __name__ == "__main__":
    main()
