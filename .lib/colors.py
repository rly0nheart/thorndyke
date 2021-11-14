import sys

colors = True
platf = sys.platform
if platf.lower().startswith(("os", "win", "darwin","ios")): 
    colors = False

if not colors:
	red = white = green = yellow = reset = ""

else:                                                 
    red = "\033[91m"
    white = "\033[97m"
    green = "\033[92m"
    yellow = "\033[93m"
    reset = "\033[0m"
