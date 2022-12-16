import os
import sys

def start(first_name):
    return open(os.path.join(sys.path[0], "text/start.html"), "r").read().replace("{{first_name}}", first_name)

def tasks():
    return open(os.path.join(sys.path[0], "text/tasks.html"), "r").read()

def referral():
    return open(os.path.join(sys.path[0], "text/referral.html"), "r").read()

def about():
    return open(os.path.join(sys.path[0], "text/about.html"), "r").read()
