import sys
from robojiro.kj import KJ


def main():
    kj = KJ()
    while True:
        line = sys.stdin.readline().trim()
        if line == "exit":
            print("Bye")
            break
        elif line == "":
            continue
        kj.push(line)
        print("result: " + kj.abstraction())


if __name__ == "__main__":
    main()
