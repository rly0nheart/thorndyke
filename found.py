import os
import sys
sys.path.append(os.getcwd()+"/.lib/")
from colors import red,white,green,reset

# The found function returns found results only
# And it can be called by specifying the -f/--found flags        
def found(args,response,site_name,site_url,data):
    if response.status_code == 200:      
        print(f'\n{white}{site_name}{reset}')
        for key,value in data.items():
        	print(f'{white}├─ {key}: {green}{value}{reset}')
