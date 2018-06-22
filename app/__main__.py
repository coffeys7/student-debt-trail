import sys
from classmodule import Loan
from funcmodule import my_function

def main():
    args = sys.argv[1:]
    print('arg count :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))

if __name__ == '__main__':
    main()
