import os
import sys
sys.path.append(os.getcwd()+"/.lib/")
from colors import red,white,green,reset

# The notfound function returns not found results only
# And it can be called by specifying the -n/--not-found flags
def not_found(args,response,site_name,site_url,data):
    if response.status_code != 200:
        print(f'\n{white}{site_name}{reset}')
        for key,value in data.items():
            print(f'{white}├─ {key}: {red}{value}{reset}')
