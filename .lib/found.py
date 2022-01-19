import os
import sys
sys.path.append(f'{os.getcwd()}/.lib/')
from colors import green,white,reset

# The found function returns found results only
# And it can be called by specifying the -f/--found flags        
def found(args,response,site_name,site_url):
    if response.status_code == 200:      
        print(f'{white}[{green}+{white}] {site_name}: {green}{site_url.format(args.username)}{reset}')
