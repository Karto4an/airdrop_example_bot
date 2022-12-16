import os
import sys

def start(first_name):
    return open(os.path.join(sys.path[0], "text/start.html"), "r").read().replace("{{first_name}}", first_name)