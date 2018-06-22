import os
import random
from time import sleep


def actGen():
    return 21 + random.randint(-15,15)


def print_out_beginning():
    print("\t*********************************")
    print("\t************Hello There**********")
    print("\t*********************************")
    sleep(2)
    os.system("clear")

    print("\t Welcome to College Debt Simulator")
    sleep(1)
    os.system("clear")
    return;

def actPrintout(actIn):
    if actIn > 30:
        print("\tYou paid a lot of attention in high school, and always did your work. As a result your ACT was " + str(actIn))
        return True
    else:
        print("\tYou spent a lot more time having fun in high school, so your work ethics and grades suffered. As a result your ACT was " + str(actIn))
        return False

def determine_Debt(actIn):
    if act_score > 30:
        #scholarship
        print("\t Because of your good grades and score, your private school gave you enough scholarships to cut down on your loans.")
    else:
        #super_debt
        print("bleh")

def beginning_text(actIn):
    print_out_beginning()
    name = input("\tWhat's your name? ")
    print("\tWelcome to college " + str(name))
    actScore = actIn
    got_scholarships = actPrintout(actScore)
    return name


