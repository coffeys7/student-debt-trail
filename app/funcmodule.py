import random
from classmodule import Information 

def my_function(text_to_display):
    print('text from my_function :: {}'.format(text_to_display))

    
def random_events(person_info):
    scenarios = [{"event": "You got hit by a school bus, oh shit! You're down ", "$amount" : -8000 , 
    "health" : -50, "mental_health" : -20, "grades" : 1.0},
    {"event": "Wow! You went to all of the office hours and made dean's list this semester! You're up ", "$amount" : 0 , 
    "health" : 10, "mental_health" : 15, "grades" : 1.3},
    {"event": "Look at you, you're in L-O-V-E. Goddamn, you've never been this happy in your life!!\
    You even put aside your schoolwork to spend time with that special someone. Your S.O had a birthday last weekend\
    and DAMN you showed up with the party planning...using your own pocket money.", "$amount" : -50 , 
    "health" : 20, "mental_health" : 25, "grades" : 0.85},
    {"event": "HOLY SHIT YOU HAVE BEEN AN AMAZING STUDENT. You've been involved\
    in extracurriculars and scored yourself an internship at Amazon! Go you.", "$amount" : 3000 , 
    "health" : 10, "mental_health" : 15, "grades" : 1.5}]
    event = random.choice(scenarios)
    person_info.changeCash(event["$amount"])
    person_info.changeHealth(event["health"],event["mental_health"])  
    person_info.changeGrade(event["grades"])
    event_num = scenarios.index(event)
    print(event["event"],event["$amount"]," dollars!")
    print("health :",event["health"],"\nmental health :",event["mental_health"],"\ngrades : ",event["grades"])
    
    return event_num    