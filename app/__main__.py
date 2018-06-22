import sys
from classmodule import Loan
from classmodule import Options
from classmodule import Information
from funcmodule import random_events
from funcmodule import my_function
import os
import random
from time import sleep
from driver import beginning_text, actGen 


def main():
    args = sys.argv[1:]
    print('arg count :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))
    #act_score = actGen()
    act_score = 23
    person = beginning_text(act_score)
    person_info = Information(person)   
    random_events(person_info)

if __name__ == '__main__':
    main()
