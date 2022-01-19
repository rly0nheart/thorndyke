#!/usr/bin/env python3

import os
import sys
import urllib3
import random
import argparse
import requests
from tqdm import tqdm
from datetime import datetime
sys.path.append(os.getcwd()+"/.lib/")
from colors import red,white,green,yellow,reset
import sites, banner, headers, found, not_found, default_lookup


def Thorndyke():
    start_time = datetime.now()
    parser = argparse.ArgumentParser(description=f'{white}Lightweight username enumeration tool',epilog=f'{white}Thorndyke checks the availability of a specified username on over 200 popular websites{white}. Developed by Richard Mwewa | https://github.com/{green}rly0nheart{reset}')
    parser.add_argument('username', help=f'{green}target username{reset}')
    parser.add_argument('--file', help=argparse.SUPPRESS)
    parser.add_argument('--found', dest='found', help=f'{white}return found results only{reset}', action='store_true')
    parser.add_argument('--not-found', dest='notfound', help=f'{white}return not found results only{reset}', action='store_true')
    parser.add_argument('--output', dest='output', metavar=f'{white}path/to/file{reset}', help=argparse.SUPPRESS)
    parser.add_argument('--version',version=f'{white}2022.0.6.0 Released on 20nd January 2022{reset}',action='version')
    args = parser.parse_args()
    print(banner.banner)
    
    	
    print(f'{white}[{green}~{white}] Enumerating @{green}{args.username}{white} on:{reset}')
    for site_name, site_url in tqdm(sites.database.items()):
        try:
            # Suppressing HTTPS warnings
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            user_agent = {'User-Agent': f'{random.choice(headers.user_agents)}'}
            response = requests.get(site_url.format(args.username), headers=user_agent, verify=False, allow_redirects=False)
            if response.status_code == 200:
            	status = 'Found'
            else:
            	status = 'Not Found'
            data = {'Status': status,
                         'Username': args.username,
                         'URL': f"{site_url.format(args.username)}",
            }
            if args.found:
            	found.found(args,response,site_name,site_url,data)
            elif args.notfound:
            	not_found.not_found(args,response,site_name,site_url,data)
            else:
            	default_lookup.default(args,response,site_url,site_name,data)
           	
        except KeyboardInterrupt:
            exit(f'\n{white}[{red}!{white}] Process interrupted with {red}Ctrl{white}+{red}C{reset}')
            
        except requests.exceptions.ReadTimeout:
            print(f'{white}{site_name}: {yellow}Request Timed Out{reset}')
            
        except Exception as e:
            print(f'{white}{site_name}: {red}{e}{reset}')
            
    print(f'{white}[{green}-{white}] Finished in {green}{datetime.now()-start_time}{white} seconds.{reset}')
