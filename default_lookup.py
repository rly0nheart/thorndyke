import os
import sys
sys.path.append(os.getcwd()+"/.lib/")
from colors import red,white,green,reset

# The normal function will return both found and not found results
# This is called by default if both the  -f/--found & -n/--not-found flags are not specified
def default(args,response,site_url,site_name,data):
    if response.status_code == 200:
    	print(f'\n{white}{site_name}{reset}')
    	for key,value in data.items():
    	    print(f'{white}├─ {key}: {green}{value}{reset}')   
    else:
        color = red
        print(f'\n{white}{site_name}{reset}')
        for key,value in data.items():
            print(f'{white}├─ {key}: {red}{value}{reset}')
