import sys

def main():
    # Argument handling
    if len(sys.argv) != 2:
        sys.exit("Usage: python lines.py 'path'")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Path must be to a .py file")

    # Access file and print lines of code
    try:
        with open(sys.argv[1]) as code:
            count = 0
            for line in code:
                if len(line.strip()) >= 1 and not line.strip().startswith("#"):
                    count += 1
    except FileNotFoundError:
        sys.exit("File not Found")

    print(count)

main()