import os
import sys
sys.path.append(f'{os.getcwd()}/.lib/')
from colors import red,white,reset

# The notfound function returns not found results only
# And it can be called by specifying the -n/--not-found flags
def not_found(args,response,site_name,site_url):
    if response.status_code != 200:
    	print(f'{white}[{red}-{white}] {site_name}: {red}Not Found{reset}')
