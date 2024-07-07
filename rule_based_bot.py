# rule based chatbot

import random

#negative responses

negative_responses=["no","nop","nope","na","nah"]

#exit commands

exit_commands=["c ya","later","hasta la vista","bye","stop","tata"]

# random starter questions

random_questions=["y u here?\t", "u lonely, want company?\t", "hey there, how ya doin?\t"]

#words to look out for

keywords=["what","why","how"]

#function which exits the program

def make_exit(reply):
    for command in exit_commands:
        if command in reply:
            print("\nokay thanks😄👋")
            return True

# function which returns specific responses based on keywords  
def match_reply(reply):
    for key in keywords:
        found_match=True if key in reply else False
        if found_match and key=='what':
            return random.choice(["\n I want to learn, like a lot📖📖\t","\n am curious about things\t"])
        elif found_match and key=='why':
            return random.choice(["\n me autistic🤧\t", "\nmeanie ask mean things😭😭😭\t"])
        elif found_match and key=='how':
            return random.choice(["\n🌴 coconut fell my head\t","\nbad memory, I afraid😨\t"])
    if not found_match:
        return random.choice(["\nteach me more, 📖📖 me learn\t","\ni love studying, but i forget🤧\t"])


name=input("watcha name?\t")
will_help=input(f"Hi {name}, am jarvis_noob will you help me learn?\t")
if will_help in negative_responses:
    print("\n 😭😭😭😭 you meanie 😭😭😭\n")
    exit()
else:
    reply=input(random.choice(random_questions)).lower()
    while not make_exit(reply):
        reply=input(match_reply(reply))



