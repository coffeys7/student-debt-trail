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


def start_semester(person_in):
    count = 10
    while count > 0:
        print("\t Week: " + str(10 - count))
        print("\t ......")
        sleep(1)
        random_events(person_in)
        count = count - 1

def main():
    args = sys.argv[1:]
    print('arg count :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))
    #act_score = actGen()
    act_score = actGen()
    person = beginning_text(act_score)
    person_info = Information(person)   
    start_semester(person_info)

if __name__ == '__main__':
    main()
