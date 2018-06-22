import sys
from classmodule import Loan
from classmodule import Options
from classmodule import Information
from funcmodule import random_events
import os
import random
from time import sleep
from driver import beginning_text 


def main():
    args = sys.argv[1:]
    print('arg count :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))
    #act_score = actGen()
    act_score = 23
    person = beginning_text(act_score)
    if act_score > 30:
        #scholarship
        print("Oh no")
    else:
        #super_debt
        print("Oh yis")

    person_info = Information(person)   
    random_events(person_info)

if __name__ == '__main__':
    main()
