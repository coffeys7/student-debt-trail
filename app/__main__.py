import sys
from classmodule import Loan
from classmodule import Information
from funcmodule import my_function
import os
import random
from time import sleep
from driver import beginning_text 


def main():
    args = sys.argv[1:]
    print('arg count :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))
    act_score = actGen()
    person = beginning_text(act_score)
    if act_score > 30:
        #scholarship
    else:
        #super_debt

    person_info = Information(person)    


if __name__ == '__main__':
    main()
