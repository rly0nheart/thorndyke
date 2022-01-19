import os
import sys
sys.path.append(f'{os.getcwd()}/.lib/')
from colors import red,white,green,reset

# The normal function will return both found and not found results
# This is called by default if both the  -f/--found & -n/--not-found flags are not specified
def default(args,response,site_url,site_name):
    if response.status_code == 200:
    	print(f'{white}[{green}+{white}] {site_name}: {green}{site_url.format(args.username)}{reset}')
    else:
    	print(f'{white}[{red}-{white}] {site_name}: {red}Not Found{reset}')
