import sys
from classmodule import Loan
from classmodule import Options
from classmodule import Information
from funcmodule import my_function
import os
import random
from time import sleep
from driver import beginning_text, actGen 


def main():
    args = sys.argv[1:]

    # Options exampls
    # ls = ['One', 'Two', 'Three']
    # options = Options(ls, 'Which number do you want?')
    # opt = options.select()
    print('arg count :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))
    act_score = actGen()
    person = beginning_text(act_score)

    person_info = Information(person)    


if __name__ == '__main__':
    main()
