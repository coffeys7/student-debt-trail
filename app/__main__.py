import sys
from .classmodule import MyClass
from .funcmodule import my_function

def main():
    args = sys.argv[1:]
    print('arg count :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))

    my_object = MyClass('Some string')

if __name__ == '__main__':
    main()
